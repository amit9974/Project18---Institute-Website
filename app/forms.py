from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Create Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    # validate user
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError('Username already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('Email is already exists')
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('User is not exists')
        return username
