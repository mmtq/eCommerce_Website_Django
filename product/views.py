from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def product(request):
    return render(request, 'product/product.html')