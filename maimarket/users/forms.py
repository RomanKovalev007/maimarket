from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Введите логин', 'class': 'form__input'}))
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

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=None, label='Логин')

    class Meta:
        model = get_user_model()

        fields = ['photo', 'first_name', 'last_name', 'username', 'number', 'email']
        labels = {
            'username': 'Логин',
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'number': 'Номер телефона'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Введите номер телефона'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите электронную почту'})
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'placeholder':'Введите старый пароль'}))
    new_password1 =forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'placeholder':'Введите новый пароль'}))
    new_password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

