from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base', views.base, name="base"),
    path('test', views.test, name="test"),
    path('customers', views.customers, name="customers"),
    path('add_customer', views.add_customer, name="add_customer"),
]