from django.db import models
from django.db.models import Sum

ORDER_STATUS_CHOICES = (
    # Awaiting confirmation
    ('aw','در انتظار تایید'),
    # Processing
    ('p','درحال پردازش'),
    # Ready to send
    ('r','اماده ارسال از انبار'),
    # Delivery
    ('d','تحویل پست داده شده'),
    ('do','تحویل مشتری داده شد'),)
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='Product', null=True)
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Brad(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=50, null=True)
    image = models.ImageField(upload_to='Product/brand', null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='cat')
    image_1 = models.ImageField(upload_to='Product', null=True)
    image_2 = models.ImageField(upload_to='Product', null=True)
    image_3 = models.ImageField(upload_to='Product', null=True)
    Brad = models.ForeignKey(Brad, on_delete=models.CASCADE,null=True, related_name='brand')
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey('Account.User', on_delete=models.CASCADE,related_name='order')
    products = models.ManyToManyField(Product, related_name='products')
    status = models.CharField(max_length=2,choices=ORDER_STATUS_CHOICES)
    total_price = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)