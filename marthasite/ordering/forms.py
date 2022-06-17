from socket import fromshare
from django import forms

class PlaceNewOrder(forms.Form):
    rice = forms.BooleanField(required=False)
    rotty = forms.BooleanField(required=False)
    noodles = forms.BooleanField(required=False)
    wadei = forms.BooleanField(required=False)
    dhal = forms.BooleanField(required=False)
    fish = forms.BooleanField(required=False)
    watalappam = forms.BooleanField(required=False)
    jelly = forms.BooleanField(required=False)
    pudding = forms.BooleanField(required=False)