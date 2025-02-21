from django.shortcuts import render, redirect
from django.db.models import Q
from product.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from order.models import Order
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


@login_required
def profile(request):
    orders = request.user.orders.all()
    for order in orders:
        print(order.created_at)
    return render(request, 'core/profile.html', {'orders': orders})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Profile updated successfully')
        
        return redirect('profile')
            
    return render(request, 'core/edit_profile.html')