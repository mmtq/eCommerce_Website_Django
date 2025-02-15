from django.shortcuts import render
from django.db.models import Q
from product.models import Product, Category
# Create your views here.

def index(request):
    products = Product.objects.all()[:8]
    
    context = {
        'products': products
    }
    return render(request, 'core/frontpage.html', context)

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category')
    if active_category:
        products = products.filter(category__slug=active_category)
    
    query = request.GET.get('query')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    return render(request, 'core/shop.html', context)