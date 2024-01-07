from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    shopping_cart = models.ManyToManyField('Store.Product', related_name='item', blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True, null=True)
    address = models.TextField(null=True)
    registered = models.BooleanField(null=True)
    # جک کردن پر بودن ادرس کاربر
    def check_address(self):
        if self.address:
            return True
        else:
            return False
    # چک کرد پر بودن شماره تلفن کاربر
    def check_phone_number(self):
        if self.phone_number:
            return True
        else:
            return False
    # چک کردن پر بودن لیست خرید کاربر
    def check_shopping_cart(self):
        if self.shopping_cart:
            return True
        else:
            return False

class Otp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.PositiveSmallIntegerField(null=True)
    expiration_date = models.DateTimeField(null=True)
    def __str__(self):
        return f'User: : "{self.user.username}" Otp_code: {self.otp}'