from audioop import reverse

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from goods.models import Goods
from users.forms import LoginUserForm, RegisterForm, ProfileUserDataChangeForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:register_done')

def register_done(request):
    return render(request, 'users/register_done.html')


class ProfileUserDataChange(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserDataChangeForm
    template_name = 'users/profile_change_data.html'
    extra_context = {'title': 'Профиль пользователя'}
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change.html'

def profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    return render(request, 'users/profile.html', {'user': user})



@login_required
def profile_user(request):
    ads = Goods.objects.filter(seller=request.user)
    data = {'ads': ads}
    return render(request, 'users/my_profile.html', data)

