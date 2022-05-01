from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomSupplierCreationForm,AddressForm
from .models import MyUser,UserAddressInfo
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView,LogoutView,UserModel
from django.contrib.auth import get_user_model
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

# class SignUpPage(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def SignUpPage(request):
    
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if user_form.is_valid() and address_form.is_valid():

            user_form.save()
            x = MyUser.objects.last()
            address_form.UserId = x
            y = address_form.data['address']
            info = UserAddressInfo(UserId = x,address=y)
            info.save()
            return HttpResponseRedirect('/user/login')    

        else:
            context = {
                'user_form': user_form,
                'address_form': address_form,
            }
    else:
        context = {
            'user_form': MyUser(),
            'address_form': UserAddressInfo(),
        }
        
    return render(request, 'signup.html', context)



# class SupplierSignUpPage(generic.CreateView):
#     form_class = CustomSupplierCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'supplier_signup.html'

def SupplierSignUpPage(request):
    
    if request.method == 'POST':
        user_form = CustomSupplierCreationForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if user_form.is_valid() and address_form.is_valid():

            user_form.save()
            x = MyUser.objects.last()
            address_form.UserId = x
            y = address_form.data['address']
            info = UserAddressInfo(UserId = x,address=y)
            info.save()
            return HttpResponseRedirect('/user/login')    

        else:
            context = {
                'user_form': user_form,
                'address_form': address_form,
            }
    else:
        context = {
            'user_form': MyUser(),
            'address_form': UserAddressInfo(),
        }
        
    return render(request, 'supplier_signup.html', context)





def LoginType(request):
    return render(request,'login.html')


class UserLogin(LoginView):
    template_name = 'login_user.html'


class UserLogout(LogoutView):
    template_name = 'user_logout.html'


class UserInfoPanel(DetailView):
    model = UserAddressInfo
    template_name = 'userHome.html'
    context_object_name = 'selected_user'
    
