import Account.models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """
         ساختن و ذخیره یک کاربر با استفاده از password  و phone_number
        """
        if not phone_number:
            raise ValueError("The given phone_number must be set")

        GlobalUserModel = Account.models.User(
            self.model._meta.app_label, self.model._meta.object_name
        )

        username = f"user_{phone_number}"  # تعیین مقدار username بر اساس شماره تلفن
        user = self.model(phone_number=phone_number, username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user( phone_number, password, **extra_fields)
class User(AbstractUser):
    user_name = None
    email = None
    shopping_cart = models.ManyToManyField('Store.Product', related_name='item', blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True, null=True)
    address = models.TextField(null=True)
    registered = models.BooleanField(null=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
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

    def check_registered(self):
        if self.registered:
            return True
        else:
            False

class Otp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.PositiveSmallIntegerField(null=True)
    expiration_date = models.DateTimeField(null=True)
    def __str__(self):
        return f'User: : "{self.user.phone_number}" Otp_code: {self.otp}'