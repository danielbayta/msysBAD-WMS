from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name="base"),
    path('', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"), 
    path('user_register', views.user_register, name="user_register"),
    path('home', views.home, name="home"),
    path('customers', views.customers, name="customers"),
    path('add_customer', views.add_customer, name="add_customer"),
    path('update_customer/<customer_id>', views.update_customer, name="update_customer"),
    path('delete_customer/<customer_id>', views.delete_customer, name="delete_customer"),
    path('inventory', views.inventory, name="inventory"),
    path('add_inventory', views.add_inventory, name="add_inventory"),
    path('update_inventory/<inventory_id>', views.update_inventory, name="update_inventory"),
    path('delete_inventory/<inventory_id>', views.delete_inventory, name="delete_inventory"),
]