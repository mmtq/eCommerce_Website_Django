from django.shortcuts import render
from product.models import Product, Category
# Create your views here.

def index(request):
    products = Product.objects.all()[:8]
    
    context = {
        'products': products
    }
    return render(request, 'core/frontpage.html', context)