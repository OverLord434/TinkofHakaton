from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from .models import User


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': 'Введите имя',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': 'form-control',
            'placeholder': 'Введите пароль',
        })
    )
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя',
        })
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш email',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите пароль',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует!')
        return email

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "username",
            "email",)

    image = forms.ImageField(required=False)
    username = forms.CharField()
    email = forms.CharField()
