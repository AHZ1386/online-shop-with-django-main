from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='Product', null=True)
    slug = models.SlugField(max_length=50, null=True)

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
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey('Account.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='products')
