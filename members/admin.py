from django.contrib import admin
from . models import Order,OrderItem, Customer, ShippingAddress
# regsiter to admin panel
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
