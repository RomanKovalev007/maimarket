import random

from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from favorites.models import Favorites
from goods.models import Goods
from maimarket import settings
from users.forms import LoginUserForm, RegisterForm, ProfileUserDataChangeForm, UserPasswordChangeForm, VerificationForm
from users.models import EmailVerification


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('users:register_done')

class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:register_done')

def register_done(request):
    return render(request, 'users/register_done.html')

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    extra_context = {'title': 'Изменение пароля'}
    template_name = 'users/password_change.html'

class ProfileUserDataChange(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserDataChangeForm
    template_name = 'users/edit_profile.html'
    extra_context = {'title': 'Профиль пользователя'}
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileUserDataChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile', user_id=request.user.id)
    else:
        form = ProfileUserDataChangeForm(instance=user)

    context = {
        'form': form,
        'user': user,
        'title': 'Редактирование профиля'
    }

    return render(request, 'users/edit_profile.html', context)


def profile_goods(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    ads = Goods.objects.filter(seller=user, is_published=1)
    data = {'ads': ads,
            'user': user,
            'title': f'Профиль {user.username}'}
    return render(request, 'users/profile.html', data)


def profile_not_published(request):
    ads = Goods.objects.filter(seller=request.user, is_published=0)
    data = {'ads': ads, 'title': f'Профиль {request.user.username}'}
    return render(request, 'users/profile.html', data)




@login_required
def profile_user(request):
    ads = Goods.objects.filter(seller=request.user, is_published=1)
    data = {'ads': ads}
    return render(request, 'users/my_profile.html', data)




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 1. Сохраняем данные во временную сессию (не в БД!)
            request.session['temp_user'] = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],  # Пароль уже захэширован
                'code': str(random.randint(100000, 999999)),
            }

            # 2. Отправляем код на email
            send_mail(
                'Код подтверждения',
                f'Ваш код: {request.session["temp_user"]["code"]}',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            # 3. Перенаправляем на страницу ввода кода
            return redirect('users:verify_email')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def verify_email(request):
    if 'temp_user' not in request.session:
        return redirect('register')  # Если нет данных, возвращаем на регистрацию

    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            user_code = form.cleaned_data['code']
            saved_code = request.session['temp_user']['code']

            if user_code == saved_code:
                # Код верный → создаем пользователя
                get_user_model().objects.create_user(
                    username=request.session['temp_user']['username'],
                    email=request.session['temp_user']['email'],
                    password=request.session['temp_user']['password'],
                )
                del request.session['temp_user']  # Очищаем сессию
                return redirect('users:register_done')  # Перенаправляем на вход
            else:
                # Код неверный – ошибка
                return render(request, 'users/verify_email.html', {
                    'form': form,
                    'error': 'Неверный код. Попробуйте снова.',
                })
    else:
        form = VerificationForm()

    return render(request, 'users/verify_email.html', {'form': form})