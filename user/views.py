from django.shortcuts import render
from .forms import CustomUserCreationForm,CustomSupplierCreationForm
from .models import Customer,Supplier,CustomerAddresInfo
from django.contrib.auth import authenticate,login
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class SignUpPage(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def LoginType(request):
    return render(request,'login.html')


class SupplierSignUpPage(generic.CreateView):
    form_class = CustomSupplierCreationForm
    success_url = reverse_lazy('login')
    template_name = 'supplier_signup.html'