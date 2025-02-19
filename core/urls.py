from django.urls import path
from core.views import index, shop, profile, edit_profile

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]