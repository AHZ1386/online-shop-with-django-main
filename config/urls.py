from django.contrib import admin
from django.urls import path,include
from .views import test
from Payment import views as pay
from azbankgateways.urls import az_bank_gateways_urls
from Account import views as Accounts
from django.conf import settings
from django.conf.urls.static import static
from Store import views as Store
urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path("", test,name='index'),
    # Account
    
    
    path("add-to-cart/<int:id>",Accounts.add_to_cart , name='add_to_cart'),
    path("remove-from-art/<int:id>",Accounts.remove_from_cart , name='remove_from_cart'),
    path("account/", include('Account.urls') ),
    # path("login/", Accounts.UserLoginView.as_view(), name='login'),
    
    
    
    # Payment

    path('go-to-getway/',pay.go_to_gateway_view,name='go-to-getway'),
    
    
    # path('buy/',views.create_order),
    path('callback-gateway/', pay.callback_gateway_view,name='callback-gateway'),
    
    # Store
    path('product/',include('Store.urls')),
    path('category-list/', Store.CategoryListView.as_view(), name='category_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
