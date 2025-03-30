from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.filter(category = 2)

    return render(request, 'home.html', {'products':products})