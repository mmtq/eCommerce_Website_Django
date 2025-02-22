from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Review
# Create your views here.

def product(request, slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        user = request.user
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.create(product=product, created_by=user, rating=rating, comment=comment)
    
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)