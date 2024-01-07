from datetime import timedelta
from Store.models import Product
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.views.generic import CreateView, UpdateView
from random import randint
from .forms import UserCreateForm, UserProfileForm,OtpForm
from .models import User
from .models import Otp
from django.contrib.auth import login
from django.utils import timezone

def generate_otp(user):
    otp_expiry = timezone.now() + timedelta(seconds=120)
    otp_code = randint(1000,9999)
    otp = Otp.objects.create(user=user,otp=otp_code,expiration_date=otp_expiry)
    print(otp_code)

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        # username = form.cleaned_data.get('username')
        # phone_number = form.cleaned_data.get('phone_number')
        # password1 = form.cleaned_data.get('password1')
        # password2 = form.cleaned_data.get('password2')
        if form.is_valid():
            user = form.save()
            login(request,user)
            generate_otp(user=request.user)

            messages.success(request,'کد دریافت شده را وارد کنید')
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


def view_shopping_cart(request):
    shopping_cart = request.user.shopping_cart.all()
    context = {'shopping_cart': shopping_cart}
    return render(request, 'test.html', context)


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
