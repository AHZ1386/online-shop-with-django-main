from Store.models import Order
from django.shortcuts import render
from  Account.models import User
def index(request):
    context = {
        'orders': Order.objects.exclude(status='do').count(),
        'users': User.objects.all().count(),
    }
    return render(request, 'Custom_admin/index.html',context)