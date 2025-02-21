from django.conf import settings
from product.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session  # Store the session object
        cart = self.session.get(settings.CART_SESSION_ID)  # Retrieve cart from session
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}  # Create empty cart if not exists
        self.cart = cart  # Assign cart data
        
    def __iter__(self):
        for p in self.cart.keys():
            product = Product.objects.get(pk=p)
            item = self.cart[str(p)]
            item['product'] = product
            yield item  # Yield each item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}
        # else:
        #     self.cart[product_id]['quantity'] += 1
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        
        self.save()
    
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def get_total_cost(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids).values('id', 'price')

        product_prices = {str(p['id']): p['price'] for p in products}

        return sum(item['quantity'] * product_prices[str(p)] for p, item in self.cart.items())
    def get_item(self, product_id):
        return self.cart[str(product_id)]