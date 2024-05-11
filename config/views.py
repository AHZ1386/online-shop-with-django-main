from Store.models import Category, Product
from django.shortcuts import render
from django.views.generic import ListView


class InedexListView(ListView):
    model = Product
    paginate_by = 10
    context_object_name = 'products'
    template_name = 'Pages/index.html'