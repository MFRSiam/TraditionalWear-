from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Customer

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('phoneNumber',)
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields
