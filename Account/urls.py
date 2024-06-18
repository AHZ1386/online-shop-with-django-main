from django.urls import path

from .views import user_cart, profile, UserLoginView, UserProfileUpdateView,signup,register,user_orders,change_password,logout

app_name = 'Account'

urlpatterns = [

    path('profile/', profile, name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('edit-profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('singin/',signup,name='singin'),
    path('registration/',register,name='registration'),
    path('shopping-cart/', user_cart, name='shopping-cart'),
    path('orders/', user_orders, name='orders'),
    path('change-password/', change_password, name='change_password'),
    path('logout/',logout,name='logout')
]
