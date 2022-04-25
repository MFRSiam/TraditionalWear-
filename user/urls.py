from django.urls import path,include
from .views import SignUpPage,LoginType,SupplierSignUpPage,CustomerLogin,CustomerLogout
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',Login,name='individual'),
    path('signup/',SignUpPage.as_view(),name='signup'),
    path('supplier_signup/',SupplierSignUpPage.as_view(),name='supplier_signup'),
    path('login/',LoginType ,name='login'),
    path('customer_login',CustomerLogin.as_view(),name='customer_login'),
    path('logout/',CustomerLogout.as_view(),name='logout'),
    # path('<int:pk>')
]
