from dataclasses import fields
from distutils.command.upload import upload
import imp
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
# Create your models here.

"""New User Model"""
class NewUserModel(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address', error_messages={'exists':'Email ID is taken'})

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')


    def __init__(self, *args, **kwargs) -> None:
        super(NewUserModel, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


    def save(self, commit=True):
        user = super(NewUserModel, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user


    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('Email is already exists.')
        return self.cleaned_data['email']

    


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Media/Course/', null=True, blank=True)

    def __str__(self):
        return self.name

        

class PlacementPartner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/placement_partner_images/')

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Faculty_Profile(models.Model):
    image = models.ImageField(upload_to='Media/Faculty/')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    expert = models.CharField(max_length=300)
    about = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name

