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
            attrs={'placeholder' : 'Enter your email',
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
            attrs={'placeholder' : 'Enter phone number',
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
        max_value = 5, min_value = 1,
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
    table = forms.CharField()
    prefix = 'order'

class OrderItemForm(forms.Form):
    # Dynamically generate food, qty, note depending on the size of the menu
    food1 = forms.CharField()
    qty1 = forms.IntegerField()
    note1 = forms.CharField()
    food2 = forms.CharField()
    qty2 = forms.IntegerField()
    note2 = forms.CharField()
    food3 = forms.CharField()
    qty3 = forms.IntegerField()
    note3 = forms.CharField()
    food4 = forms.CharField()
    qty4 = forms.IntegerField()
    note4 = forms.CharField()
    food5 = forms.CharField()
    qty5 = forms.IntegerField()
    note5 = forms.CharField()
    prefix = 'orderItem'