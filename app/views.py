from multiprocessing import context
from unicodedata import category
from .models import BlogCategories, Course, CourseCategory, Faculty_Profile, Contact, Posts, Tags
from django.shortcuts import redirect, render
from .models import NewUserModel
from django.contrib.auth import authenticate, login
from django.contrib import messages
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
def Register(request):
    category = CourseCategory.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        form = NewUserModel(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('hompage')
    else:
        form = NewUserModel()
    context={
        'form':form,
        'category':category,
        'course':course,
    }
    return render(request, 'registration/register.html', context)

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