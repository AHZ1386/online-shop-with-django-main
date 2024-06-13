from Store.models import Order, Product
from django.shortcuts import render
from  Account.models import User
from django.views.generic import ListView
def index(request):
    context = {
        'orders': Order.objects.exclude(status='do').count(),
        'users': User.objects.all().count(),
        'products': Product.objects.count(),

    }
    return render(request, 'Custom_admin/index.html',context)

# TODO create manage_orders page
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

# TODO create product_actegorise manage page
def product_categories(request):
    pass
