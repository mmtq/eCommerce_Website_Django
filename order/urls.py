from django.urls import path
from .views import start_order, payment_success
urlpatterns = [
    path('start-order/', start_order, name='start_order'),
    path('success/', payment_success, name='payment_success'),
]