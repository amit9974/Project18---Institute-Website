from multiprocessing import reduction
from operator import imod
from .models import BlogCategories, Course, CourseCategory, Faculty_Profile, Contact, Posts, Tags, Certificate
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
# Create your views here.

"""Homepage"""
def HomePage(request):
    category = CourseCategory.objects.all()
    course = Course.objects.all()
    faculty = Faculty_Profile.objects.all()
    context={
        'category':category,
        'course':course,
        'faculty':faculty,
    }
    return render(request, "index.html", context)


"""Add New User"""
def UserRegisterView(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, 'Registration Success')
            return redirect('login')
        else:
            messages.error(request, 'Username or Password is incorrect')
    ctx = {'form':form, 'title':'Registration'}
    return render(request, 'registration/register.html', ctx)


def UserLoginView(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Success')
            return redirect('/')
        else:
            messages.error(request, 'Wrong Credentials !')
    ctx ={'form':form, 'title':'Login'}
    return render(request, 'registration/login.html', ctx)

def UserLogoutView(request):
    logout(request)
    return redirect('/')
    

"""Contact Page"""
def ContactPage(request):
    category = CourseCategory.objects.all()
    course = Course.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_message = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        new_message.save()
        messages.success(request, 'Your message has been send succesfully')
        return redirect('contact')
    else:
        form = Contact()
    context={
        'category':category,
        'course':course,
        'form':form
    }
    return render(request, 'contact.html', context)


"""Details Page"""
def DetailsPage(request, id):
    course = Course.objects.filter(id=id)
    category = CourseCategory.objects.all()
    c = Course.objects.all()
    context={
        'course':course,
        'category':category,
        'c':c,
    }
    return render(request, 'courses/details.html', context)

"""About Page"""
def AboutPage(request):
    course = Course.objects.all()
    category = CourseCategory.objects.all()
    context={
        'category':category,
        'course':course,
    }

    return render(request, 'about.html', context)


"""Blog Page"""
def blogPage(request):
    category = CourseCategory.objects.all()
    course = Course.objects.all()
    cat = BlogCategories.objects.all()
    post = Posts.objects.all()[0:6]
    tag = Tags.objects.all()
    context = {
        'category':category,
        'course':course,
        'cat':cat,
        'post':post,
        'tag':tag,
    }
    return render(request, 'blog/blog.html', context)

def BlogDetail(request):
    category = CourseCategory.objects.all()
    course = Course.objects.all()
    cat = BlogCategories.objects.all()
    context = {
        'category':category,
        'course':course,
        'cat':cat,
    }
    # blog = Course.objects.filter(id=id)
    # ctx={
    #     'blog':blog,
    # }
    return render(request, 'blog/blog_detail.html', context)



def VerifyCert(request, roll_number):
    cert = Certificate.objects.filter(roll_number=roll_number)
    ctx={
        'cert':cert
    }
    return render(request, 'certficate_verify/verify.html',ctx)