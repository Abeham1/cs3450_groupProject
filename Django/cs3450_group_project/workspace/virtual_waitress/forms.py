from django import forms
from .models import Review, Menu
import datetime

class ReviewForm(forms.ModelForm):
    menuItem = forms.ModelChoiceField(Menu.objects.all())
    name = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(
            attrs={'placeholder' : 'Enter your name',
            'display': 'block',
            'width': '100%',
            'padding': '0.375rem 0.5rem',
            'font-size': '0.9375rem',
            'line-height': '1.5',
            'color': '#495057',
            'background-color': '#fff',
            'background-clip': 'padding-box',
            'border': '1px solid #ccc',
            'border-radius': '0',
            'transition': 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'}))
    email = forms.CharField(        
        max_length=60, 
        widget=forms.TextInput(
            attrs={'placeholder' : 'Enter your email address',
            'display': 'block',
            'width': '100%',
            'padding': '0.375rem 0.5rem',
            'font-size': '0.9375rem',
            'line-height': '1.5',
            'color': '#495057',
            'background-color': '#fff',
            'background-clip': 'padding-box',
            'border': '1px solid #ccc',
            'border-radius': '0',
            'transition': 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'}))
    phone = forms.CharField(        
        max_length=60, 
        widget=forms.TextInput(
            attrs={'placeholder' : 'Enter your phone number',
            'display': 'block',
            'width': '100%',
            'padding': '0.375rem 0.5rem',
            'font-size': '0.9375rem',
            'line-height': '1.5',
            'color': '#495057',
            'background-color': '#fff',
            'background-clip': 'padding-box',
            'border': '1px solid #ccc',
            'border-radius': '0',
            'transition': 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'}))
    starRating = forms.FloatField(
        max_value = 5, min_value = 0,
        widget=forms.NumberInput(
            attrs={'placeholder':'Enter 1-5',
            'display': 'block',
            'width': '100%',
            'padding': '0.375rem 0.5rem',
            'font-size': '0.9375rem',
            'line-height': '1.5',
            'color': '#495057',
            'background-color': '#fff',
            'background-clip': 'padding-box',
            'border': '1px solid #ccc',
            'border-radius': '0',
            'transition': 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'}))
    review = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={'placeholder':'Enter a review',
            'display': 'block',
            'width': '100%',
            'padding': '0.375rem 0.5rem',
            'font-size': '0.9375rem',
            'line-height': '1.5',
            'color': '#495057',
            'background-color': '#fff',
            'background-clip': 'padding-box',
            'border': '1px solid #ccc',
            'border-radius': '0',
            'transition': 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'}))

    class Meta:
        model = Review
        fields = ('menuItem', 'name', 'email', 'phone', 'review', 'starRating')

class NewMenuItem(forms.Form):
    menuItem = forms.CharField(max_length=60)
    menuDescription = forms.CharField(max_length=400)
    menuPrice = forms.FloatField()


#default=datetime.datetime.now()
class OrderForm(forms.Form):
    total = forms.FloatField()
    orderNumber = forms.IntegerField()
    prefix = 'order'

class OrderItemForm(forms.Form):
    # Dynamically generate food, qty, note depending on the size of the menu
    food = forms.CharField()
    qty = forms.IntegerField()
    note = forms.CharField()
    prefix = 'orderItem'