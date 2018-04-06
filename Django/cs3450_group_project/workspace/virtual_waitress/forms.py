from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
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
    starRating = forms.FloatField()
    review = forms.CharField(max_length=250)
    
    class Meta:
        model = Review
        fields = ('name', 'email', 'phone')

class NewMenuItem(forms.Form):
    menuItem = forms.CharField(max_length=60)
    menuDescription = forms.CharField(max_length=400)
    menuPrice = forms.FloatField()
