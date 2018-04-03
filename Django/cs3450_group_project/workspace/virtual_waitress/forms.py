from django import forms

class NewMenuItem(forms.Form):
    menuItem = forms.CharField(max_length=60)
    menuDescription = forms.CharField(max_length=400)
    menuPrice = forms.FloatField()
