from django import forms

class ReviewFrom(forms.Form):
    Review= forms.IntegerField(max_value=10)
    Description = forms.CharField(max_length=150)