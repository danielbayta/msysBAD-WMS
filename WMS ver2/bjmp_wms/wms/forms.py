from dataclasses import fields
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'contact_number', 'email')
        labels = {
            'name': '',
            'address': '',
            'contact_number': '',
            'email': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juan Dela Cruz'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'12 St. Three Village Four City'}),
            'contact_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'09123456789'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'everbody_loves@juan.com'}),
        }

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **Kwargs):
        super(RegisterUserForm, self).__init__(*args, **Kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('name', 'type', 'description', 'unit_price', 'quantity', 'reorder_level', 'reorder_date')
        labels = {
            'name': 'Name',
            'type': 'Type',
            'description': 'Description',
            'unit_price': 'Price',
            'quantity': 'Quantity',
            'reorder_level': 'Reorder Level',
            'reorder_date': 'Reorder Date',
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item or supply'}),
        #     'type': forms.SelectMultiple(choices=TYPES),
        #     'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item description: make and model'}),
        #     'unit_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'100.00'}),
        #     'quantity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
        #     'reorder_level': forms.SelectMultiple(choices=LEVELS),
        #     'reorder_date': forms.DateInput(),
        # }