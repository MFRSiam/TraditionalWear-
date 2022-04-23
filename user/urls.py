from unicodedata import name
from django.urls import path,include
from .views import SignUpPage,LoginType,SupplierSignUpPage
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',Login,name='individual'),
    path('signup/',SignUpPage.as_view(),name='signup'),
    path('login/',LoginType ,name='login'),
    path('supplier_signup/',SupplierSignUpPage.as_view(),name='supplier_signup')
    # path('<int:pk>')
]
