from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.http import HttpResponseRedirect

def base(request):
    return render (request, "bootstrap_base.html", {})

def test(request):
    return render (request, "test_here.html")

def customers(request):
    all_customers = Customer.objects.all
    return render (request, 'customers.html', {'customers':all_customers})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render (request, "add_customer.html", {})
    else:
        return render (request, "add_customer.html", {})