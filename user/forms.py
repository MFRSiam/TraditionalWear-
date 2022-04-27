from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('phoneNumber','first_name','last_name','email',)
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields

class CustomSupplierCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        model.is_supplier = True
        fields = UserCreationForm.Meta.fields + ('phoneNumber','is_supplier')
        


class CustomSupplierChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields

