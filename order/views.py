from django.shortcuts import render,redirect
from .models import Order, OrderItem
from cart.cart import Cart
import json, stripe
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

def start_order(request):
    cart = Cart(request)
    
    data = json.loads(request.body)
    total_price = 0
    
    items = []
    
    for item in cart:
        product = item['product']
        quantity = item['quantity']
        total_price += product.price * int(quantity)
        
        obj = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': quantity,
        }
        
        items.append(obj)
        
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cart/',
    )
    
    payment_intent = session.payment_intent
    
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    place = data['place']
    zipcode = data['zipcode']
    phone = data['phone']
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
    order.payment_intent = payment_intent
    order.paid = True
    order.paid_amount = total_price
    order.save()
    
    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price= int(item['product'].price * item['quantity'])
        )
        
    return JsonResponse({'session': session, 'order': payment_intent})