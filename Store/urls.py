from django.urls import path
from .views import CategoryDetailViwe,ProductDetailViwe

app_name = 'store'


urlpatterns = [
    path('category-detail/<str:slug>/',CategoryDetailViwe.as_view(),name='category_detail'),
    path('product-detail/<str:slug>/',ProductDetailViwe.as_view(),name='product_detail'),
]
