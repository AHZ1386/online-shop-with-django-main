from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    shopping_cart = models.ManyToManyField('Store.Product', related_name='item',blank=True,null=True)
    phone_number = models.CharField(max_length=11, unique=True,null=True)
    address = models.TextField(null=True)
    
    def check_address(self):
        if self.address:
            return True
        else:
            return False

    def check_phone_number(self):
        if self.phone_number:
            return True
        else:
            return False
    def check_shopping_cart(self):
        if self.shopping_cart:
            return True
        else:
            return False
        
