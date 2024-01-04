from typing import Any
from django.db import models
from django.shortcuts import render,redirect
from Store.models import Product
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,UpdateView
from .models import User
from .forms import UserCreateForm, UserProfileForm
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class UserProfileUpdateView(UpdateView):
    model = User
    print('amir')
    template_name = 'Account/edit_profile.html'
    form_class = UserProfileForm
    success_url = '/'
    def get_object(self, queryset=None):
        return self.request.user 
        

def add_to_cart(request, id):
    try:
        product = Product.objects.get(id=id)
        request.user.shopping_cart.add(product)
        last_page = request.META.get('HTTP_REFERER')
        messages.success(request, f' کالای  {product.title} به سبد خرید اضافه شد ')

        return redirect(last_page)
    except:
        raise Http404


    
def remove_from_cart(request, id):
    try:
        product = Product.objects.get(id=id)
        request.user.shopping_cart.remove(product)
        last_page = request.META.get('HTTP_REFERER')
        messages.success(request,f'کالای {product.title} از سبد خرید حذف شد ')

        return redirect(last_page)
    except:
        raise Http404
def view_shopping_cart(request):
    shopping_cart = request.user.shopping_cart.all()
    context = {
        'shopping_cart': shopping_cart
    }
    return render(request, 'test.html', context)


def profile(request):

    return render(request,'Account/profile.html')


class UserLoginView(LoginView):
    template_name = 'Account/login.html'
    
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return super().get(request, *args, **kwargs)
        
class UserSingInView(CreateView):
    model = User
    success_url = '/'
    template_name = 'Account/singin.html'
    form_class = UserCreateForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        else:
            return super().get(request, *args, **kwargs)
