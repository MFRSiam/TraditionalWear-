from dataclasses import fields
from tkinter.tix import Form
from django import forms
from .models import Products




class ReviewFrom(forms.Form):
    Review= forms.IntegerField(max_value=10)
    Description = forms.CharField(max_length=150)

class ProductAddFrom(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Name', 'Price','Product_Type','ProductImage','Description','Brand']