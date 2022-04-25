from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomSupplierCreationForm
from .models import MyUser
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView,LogoutView,UserModel
from django.contrib.auth import get_user_model
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

class SignUpPage(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class SupplierSignUpPage(generic.CreateView):
    form_class = CustomSupplierCreationForm
    success_url = reverse_lazy('login')
    template_name = 'supplier_signup.html'


def LoginType(request):
    return render(request,'login.html')


class CustomerLogin(LoginView):
    template_name = 'login_customer.html'


class CustomerLogout(LogoutView):
    template_name = 'customer_logout.html'