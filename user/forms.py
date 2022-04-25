from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('phoneNumber',)
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields

class CustomSupplierCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('phoneNumber',)
        


class CustomSupplierChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields

