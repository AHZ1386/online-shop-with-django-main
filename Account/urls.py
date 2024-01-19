from django.urls import path

from .views import view_shopping_cart, profile, UserLoginView, UserProfileUpdateView,signup,register

app_name = 'Account'

urlpatterns = [
    path('shopping-cart/', view_shopping_cart, name='view_shopping_cart'),
    path('profile/', profile, name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('edit-profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('singin/',signup,name='singin'),
    path('registration/',register,name='registration'),
]
