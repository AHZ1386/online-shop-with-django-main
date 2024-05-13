from datetime import timedelta
from Store.models import Product
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.views.generic import CreateView, UpdateView
from random import randint
from .forms import UserCreateForm, UserProfileForm,OtpForm,ChangePasswordForm
from .models import User
from .models import Otp
from django.contrib.auth import login,logout
from django.utils import timezone
from django.db import transaction
from django.contrib.auth import update_session_auth_hash
@transaction.atomic
def generate_otp(user):
    try:
        user = User.objects.get(id=user.id)
    except User.DoesNotExist:
        return None

    exiting_otp = Otp.objects.filter(user=user,expiration_date=timezone.now()).first()
    if exiting_otp:
        print(exiting_otp.otp)
    else:
        otp_code = randint(1000,9999)
        otp = Otp.objects.create(user=user,expiration_date=timezone.now()+timedelta(seconds=120),otp=otp_code)
        print(otp)

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.registered = False
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('Account:registration'))
    else:
        form = UserCreateForm()
    return render(request, 'Account/singin.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp']
            user_otp = Otp.objects.filter(otp=otp_code).first()
            if user_otp:
                if user_otp.expiration_date < timezone.now():
                    return HttpResponse('کد اشتباه است ')
                user = get_object_or_404(User, id=user_otp.user.pk)

                user.registered = True
                user.save()
                messages.success(request,'احراز هویت با موفقیت انجام شد')
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('کد اشتباه است')
    else:
            generate_otp(request.user)
            form = OtpForm()
    return render(request, 'Account/registration.html', {'form': form})
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
        messages.success(request, f'کالای {product.title} از سبد خرید حذف شد ')

        return redirect(last_page)
    except:
        raise Http404





def profile(request):
    print(request.user.shopping_cart.all)
    return render(request, 'Account/profile.html')


class UserLoginView(LoginView):
    template_name = 'Account/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return super().get(request, *args, **kwargs)


def user_cart(request):
    user = request.user
    total_price = 0
    for item in request.user.shopping_cart.all():
        total_price += item.price
    context = {
        'products':user.shopping_cart.all(),
        'total_price': total_price
    }
    return render(request,'Account/cart.html',context)

def user_orders(request):
    user = request.user
    context = {
        'completed_orders':user.order.all().filter(status='do'),

        'processing_orders':user.order.all().exclude(status='do')
    }
    return render(request,'Account/orders.html',context)


def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request,'تغییر رمز عبور با موفقیت انجام شد')
            return HttpResponseRedirect('/')
        else:
            messages.error(request,'ارورر')

    else:
        form = ChangePasswordForm()
    return render(request,template_name='Account/chang_password.html',context={'form':form})


def login_view(request):
    logout(request)
    messages.success(request,'با موفقیت از اکانت خارج شدید')
    return HttpResponseRedirect('/')