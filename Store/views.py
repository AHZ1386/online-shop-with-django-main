from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product,Category

class ProductDetailViwe(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'Product/product_detail.html'
    
class CategoryDetailViwe(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'Product/category_detail.html'

        