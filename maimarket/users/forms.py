from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Введите логин или email', 'class': 'form__input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form__input'}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Придумайте логин', 'class': 'form__input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', 'class': 'form__input'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form__input'}))

    class Meta:
        model = get_user_model()

        fields = ['username', 'password1', 'password2', 'email']
        # 'first_name', 'last_name',  'number', 'email'
        labels = {
            'password1': 'Пароль',
            'password2': 'Повтор пароля',
            'username': 'Логин',
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'number': 'Номер телефона'
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Придумайте логин', 'class': 'form__input'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'form__input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию', 'class': 'form__input'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', 'class': 'form__input'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form__input'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Введите номер телефона', 'class': 'form__input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите электронную почту', 'class': 'form__input'})
        }
        def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email).exists():
                raise ValidationError('Пользователь с таким email уже существует')

class ProfileUserDataChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()

        fields = ['photo', 'first_name', 'last_name', 'number']
        labels = {
            'username': 'Логин',
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'number': 'Номер телефона'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'id' :"prodName", 'class': "add-product__name-input"}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию', 'id' :"prodlastname", 'class': "add-product__name-input"}),
            'number': forms.NumberInput(attrs={'placeholder': 'Введите номер телефона', 'class': "price__input", 'id':"price"}),
            'photo': forms.FileInput(attrs={'class': "photo-upload__input", 'hidden': True, 'id': "fileInput"}),
        }
        # 'hidden': True, 'accept': "image/*"

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'placeholder':'Введите старый пароль', 'class': "add-product__name-input"}))
    new_password1 =forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'placeholder':'Введите новый пароль', 'class': "add-product__name-input"}))
    new_password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': "add-product__name-input"}))

