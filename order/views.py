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

    # Include customer details in metadata (so you can retrieve them later)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url=f'http://127.0.0.1:8000/success/?session_id={{CHECKOUT_SESSION_ID}}',
        cancel_url='http://127.0.0.1:8000/cart/',
        metadata={
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'address': data['address'],
            'place': data['place'],
            'zipcode': data['zipcode'],
            'phone': data['phone'],
        }
    )

    return JsonResponse({'session': session})

def payment_success(request):
    # Get the session_id from the query parameter
    session_id = request.GET.get('session_id')

    # If there's no session_id or it's invalid, redirect back to the cart
    if not session_id:
        return redirect('cart')  # Redirect to the cart page

    try:
        # Retrieve the Stripe session
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        # Check if the payment was successful
        if session.payment_status == 'paid':
            # Access the metadata from the session
            customer_email = session.metadata.get('email', '')
            first_name = session.metadata.get('first_name', '')
            last_name = session.metadata.get('last_name', '')
            address = session.metadata.get('address', '')
            place = session.metadata.get('place', '')
            zipcode = session.metadata.get('zipcode', '')
            phone = session.metadata.get('phone', '')
            payment_intent = session.payment_intent

            # Process the order only if it's a new session and the payment was successful
            if not Order.objects.filter(payment_intent=payment_intent).exists():
                order = Order.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    first_name=first_name,
                    last_name=last_name,
                    email=customer_email,
                    address=address,
                    place=place,
                    zipcode=zipcode,
                    phone=phone,
                    paid=True,
                    paid_amount=session.amount_total / 100,
                    payment_intent=payment_intent,
                )

                cart = Cart(request)
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['quantity'],
                        price=int(item['product'].price * item['quantity'])
                    )

                # Clear the cart after the order is created
                cart.clear()

            return render(request, 'cart/success.html', {'order': order})

        else:
            # If the payment was not successful, redirect back to the cart
            return redirect('cart')

    except stripe.error.StripeError as e:
        # Handle Stripe errors (e.g., network issues, invalid session ID)
        return redirect('cart')
