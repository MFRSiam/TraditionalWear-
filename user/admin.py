from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Customer,Supplier,CustomerAddresInfo


# Register your models here.


admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(CustomerAddresInfo)