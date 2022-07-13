from ast import Or
from django.contrib import admin
from .models import MainDish, SideDishes, Dessert, Order


# Register your models here.
admin.site.register(MainDish)
admin.site.register(SideDishes)
admin.site.register(Dessert)
admin.site.register(Order)
