from django.urls import path
from . import views
app_name = 'Custom_admin'

urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.ProductListView.as_view(),name='products'),
    path('users/',views.UserListView.as_view(),name='users'),
    path('orders/',views.OrderListView.as_view(),name='orders'),
    path('create-product/',views.ProductCreateView.as_view(),name='create_product'),
    path('update-product/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('order-update/<int:pk>', views.OrderUpdateView.as_view(), name='order_update'),

]