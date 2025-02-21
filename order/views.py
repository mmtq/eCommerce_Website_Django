from django.shortcuts import render,redirect
from .models import Order, OrderItem
from cart.cart import Cart
# Create your views here.

def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        place = request.POST.get('place')
        zipcode = request.POST.get('zipcode')
        phone = request.POST.get('phone')

        order = Order.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            place=place,
            zipcode=zipcode,
            phone=phone,
        )
        
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price= int(item['product'].price * item['quantity'])
            )
        
    return redirect('profile')