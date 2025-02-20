from django.shortcuts import render
from .cart import Cart
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    product = Product.objects.get(pk=product_id)
    messages.info(request, f'Added {product.name} to cart')

    # Render cart icon
    cart_html = render_to_string('cart/menu_cart.html', {'cart': cart}, request=request)
    # Render messages
    messages_html = render_to_string('core/partials/messages.html', {'messages': messages.get_messages(request)}, request=request)

    return HttpResponse(f'{cart_html}\n{messages_html}')

# def add_to_cart(request, product_id):
#     cart = Cart(request)
#     cart.add(product_id)
#     product_name = Product.objects.get(pk=product_id).name
#     messages.info(request, f'Added {product_name} to cart')
#     # messages = messages.get_messages(request)
#     return render(request, ['cart/menu_cart.html', 'core/partials/messages.html'], {'messages': messages.get_messages(request)})

def cart(request):
    return render(request, 'cart/cart.html')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')