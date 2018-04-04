from django import forms

<<<<<<< HEAD
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'contact','starRating', 'review',)
=======
class NewMenuItem(forms.Form):
    menuItem = forms.CharField(max_length=60)
    menuDescription = forms.CharField(max_length=400)
    menuPrice = forms.FloatField()
>>>>>>> 85138683962687d06ac032cf6dc1888c994cde3d
