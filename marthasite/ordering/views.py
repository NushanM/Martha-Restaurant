from django.shortcuts import render
from .forms import PlaceNewOrder

# Create your views here.
# There are 4 views such as home, order, login, reports

def home(response):
    return render(response, "ordering/home.html", {})

def order(response):
    form = PlaceNewOrder()
    return render(response, "ordering/order.html", {"form":form})

def login(response):
    return render(response, "ordering/login.html", {})

def reports(response):
    return render(response, "ordering/report.html", {})
