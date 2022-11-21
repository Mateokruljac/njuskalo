from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = False, null = False)
    username = models.CharField(max_length=100, blank = True, null = True)
    email = models.EmailField(max_length=100, blank = True, null = True)
    
    def __str__(self):
        return self.user.username

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_finished = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.customer.username} Complete: {self.complete}"
    
    @property
    def total_items(self):
        items = self.orderitem_set.all()
        full_items = sum([item.quantity for item in items])
        return full_items
    
    @property
    def total_price(self):
        items = self.orderitem_set.all()
        full_price = sum([item.item_full_price for item in items])
        return full_price

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null = True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default = 0)
    
    
    @property
    def item_full_price(self):
        return self.quantity * self.product.price

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null= True)
    street_address = models.CharField(max_length=100)     
    city = models.CharField(max_length=100)     
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.street_address} {self.city}"     