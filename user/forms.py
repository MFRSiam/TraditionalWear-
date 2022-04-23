from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Customer,Supplier

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('phoneNumber',)
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields

class CustomSupplierCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Supplier
        fields = UserCreationForm.Meta.fields + ('address','phoneNo',)
        


class CustomSupplierChangeForm(UserChangeForm):
    class Meta:
        model = Supplier
        fields = UserChangeForm.Meta.fields

