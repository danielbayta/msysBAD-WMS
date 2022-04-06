from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.success(request, ("There was an error logging in..."))
            return redirect ('user_login')
    else:
        return render (request, 'login.html', {})
    
def user_logout(request):
    logout(request)
    messages.success(request, ("Logged out"))
    return redirect('./')

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Successfully registered!"))
            return redirect('home')
    else:
        form = UserCreationForm()  

    return render(request, 'register.html', {'form':form,})

def home(request):
    return render (request, "home.html", {})

def customers(request):
    all_customers = Customer.objects.all()
    return render (request, 'customers.html', {'customers':all_customers})

def add_customer(request):
    submitted = False
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_customer?submitted = True')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render (request, "add_customer.html", {'form':form, 'submitted':submitted})
    
def update_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        messages.success(request, ("Customer Updated!"))
        return redirect('customers')
    return render (request, "update_customer.html", {'customer': customer, 'form':form})\

def delete_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer.delete()
    messages.success(request, ("Customer Deleted!"))
    return redirect ('customers')

def inventory(request):
    all_inventory = Inventory.objects.all()
    return render (request, 'inventory.html', {'inventory':all_inventory})

def add_inventory(request):
    submitted = False
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_inventory?submitted = True')
    else:
        form = InventoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render (request, "add_inventory.html", {'form':form, 'submitted':submitted})   

def update_inventory(request, inventory_id):
    inventory = Inventory.objects.get(pk=inventory_id)
    form = InventoryForm(request.POST or None, instance=inventory)
    if form.is_valid():
        form.save()
        messages.success(request, ("Inventory Updated!"))
        return redirect('inventory')
    return render (request, "update_inventory.html", {'inventory': inventory, 'form':form})\

def delete_inventory(request, inventory_id):
    inventory = Inventory.objects.get(pk=inventory_id)
    inventory.delete()
    messages.success(request, ("Item Deleted!"))
    return redirect ('inventory')
    
def base(request):
    return render (request, "bootstrap_base.html", {})