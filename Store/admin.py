from django.contrib import admin
from .models import Product,Category,Order

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)

# 