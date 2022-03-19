from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email')
    ordering = ('name',)
    search_fields = ('name', 'address')