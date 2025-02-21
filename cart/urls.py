from django.urls import path
from cart.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('hx_menu_cart/', hx_menu_cart, name ='hx_menu_cart'),
    path('update-cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
]