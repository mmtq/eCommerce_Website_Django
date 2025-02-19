from django.urls import path
from cart.views import add_to_cart, cart, checkout

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]