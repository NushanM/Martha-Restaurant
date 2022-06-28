from django.shortcuts import render
from .forms import PlaceNewOrder
from .models import Order, MainDish, Dessert
from datetime import date
from .helpers import calculate_price

# Create your views here.
# There are 4 views such as home, order, login, reports

def home(response):
    return render(response, "ordering/home.html", {})

def order(response):
    if response.method == "POST":
        form = PlaceNewOrder(response.POST)
        if form.is_valid():
            order_data = form.cleaned_data
            Order(main_dish=MainDish.objects.get(dish= order_data["main_dish"]), wadai=order_data["wadai"], dhal=order_data["dhal"], fish=order_data["fish"], dessert=Dessert.objects.get(dessert=order_data["dessert"]), order_date=date.today(), order_value= calculate_price(order_data)).save()
    else:
        form = PlaceNewOrder()
    return render(response, "ordering/order.html", {"form":form})

def login(response):
    return render(response, "ordering/login.html", {})

def reports(response):
    return render(response, "ordering/report.html", {})
