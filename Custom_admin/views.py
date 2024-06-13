from Store.models import Order, Product
from django.shortcuts import render
from  Account.models import User
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import forms
def index(request):
    context = {
        'orders': Order.objects.exclude(status='do').count(),
        'users': User.objects.all().count(),
        'products': Product.objects.count(),

    }
    return render(request, 'Custom_admin/index.html',context)


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 10
    template_name = 'Custom_admin/order_list.html'


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 30
    template_name = 'Custom_admin/user_list.html'
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    template_name = 'Custom_admin/product_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = forms.ProductCreateForm
    template_name = 'Custom_admin/product_create.html'
    success_url = '/custom-admin/products/'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = forms.ProductUpdateForm
    template_name = 'Custom_admin/product_update.html'
    success_url = '/custom-admin/products/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'Custom_admin/product_delete.html'
    success_url = '/custom-admin/products/'