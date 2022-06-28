from socket import fromshare
from django import forms
from .models import Dessert, MainDish

main_dishes = [(main_dish.dish, main_dish.dish) for main_dish in MainDish.objects.all()]
desserts = [(dessert.dessert, dessert.dessert) for dessert in Dessert.objects.all()]
class PlaceNewOrder(forms.Form):
    main_dish = forms.CharField(label='What is the main dish?', widget=forms.Select(choices=main_dishes))
    wadai = forms.BooleanField(required=False)
    dhal = forms.BooleanField(required=False)
    fish = forms.BooleanField(required=False)
    dessert = forms.CharField(label='What is the desset?', widget=forms.Select(choices=desserts),required=False)
    # watalappam = forms.BooleanField(required=False)
    # jelly = forms.BooleanField(required=False)
    # pudding = forms.BooleanField(required=False)