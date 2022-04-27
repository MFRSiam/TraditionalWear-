from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser,UserAddressInfo


# Register your models here.


admin.site.register(MyUser)
admin.site.register(UserAddressInfo)