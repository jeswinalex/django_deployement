from django.conf.urls import url
from . import views

urlpatterns = [
    
    url('^$',views.home,name='home'),
    url('product/', views.product,name='product'),
    url('customer/', views.customer,name='customer'),
]
