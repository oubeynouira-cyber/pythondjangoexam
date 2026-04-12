from django.contrib import admin
from .models import Supplier, Client, Product, Delivery, DeliveryItem

admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(DeliveryItem)