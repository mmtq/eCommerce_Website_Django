from django.urls import path
from product.views import product

urlpatterns = [
    path('product/<str:slug>/', product, name='product'),
]