from django import forms
from .models import Rating

class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=Rating.rvalues,widget=forms.RadioSelect())

# class RatingForm(forms.Form):
#     class Meta:
#         model = Rating
#         fields = ['rating']
