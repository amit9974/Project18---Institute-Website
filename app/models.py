from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
# Create your models here.

    
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

"""Blog Categories"""
class BlogCategories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

"""Tags"""
class Tags(models.Model):
    title = models.CharField(max_length=100) 

    def __str__(self) -> str:
        return self.title

"""Posts"""
class Posts(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    post = models.TextField(max_length=500)
    img = models.ImageField(upload_to='media/post', null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.title


class Certificate(models.Model):
    roll_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    certificate = models.FileField(upload_to='Certificate/')

    def __str__(self):
        return self.roll_number
