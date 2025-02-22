from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = (
        ('ORDERED', 'Ordered'),
        ('SHIPPED', 'Shipped'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_intent = models.CharField(max_length=255, null=True, blank=True) 
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='ORDERED')
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'