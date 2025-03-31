from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    products = Product.objects.filter(category = 2)

    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in Successfully!'))
            return redirect('home')
        else:
            messages.error(request, ("There was an error! Try logging in again!"))
            return redirect('login')


    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')