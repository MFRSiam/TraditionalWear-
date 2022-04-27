from dataclasses import fields
from re import X
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import MyUser,UserAddressInfo

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('phoneNumber','first_name','last_name','email',)

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddressInfo
        fields = ('address',)


# class CustomUserCreationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField()
#     address = forms.CharField(max_length=150)
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields['password1'].label = 'Password'
#         self.fields['password2'].label = 'Password Confirmation'
#         self.fields['first_name'].label = 'First Name'
#         self.fields['last_name'].label = 'Last Name'
#         self.fields['password1'].help_text = None
#         self.fields['password2'].help_text = None
#         self.fields['address'] 
#     class Meta:
#         model = MyUser
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
#         help_texts = {
#             'username': None,
#         }
        

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = UserAddressInfo
#         fields = UserCreationForm.Meta.fields + ('address',)
        




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

