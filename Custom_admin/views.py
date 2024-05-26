from Store.models import Order
from django.shortcuts import render
from  Account.models import User
def index(request):
    context = {
        'orders': Order.objects.exclude(status='do').count(),
        'users': User.objects.all().count(),
    }
    return render(request, 'Custom_admin/index.html',context)

# TODO create manage_orders page
def orders(request):
    pass

# TODO create manage_user page
def users(request):
    pass
# TODO create manage_product page
def products(request):
    pass

# TODO create product_actegorise manage page
def product_categories(request):
    pass
