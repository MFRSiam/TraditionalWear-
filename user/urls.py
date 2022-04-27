from django.urls import path,include
from .views import SignUpPage,LoginType,SupplierSignUpPage,UserLogin,UserLogout,UserInfoPanel
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',Login,name='individual'),
    path('signup/',SignUpPage,name='signup'),
    path('supplier_signup/',SupplierSignUpPage.as_view(),name='supplier_signup'),
    path('login/',LoginType ,name='login'),
    path('user_login',UserLogin.as_view(),name='user_login'),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('user_details/<int:UserId>',UserInfoPanel.as_view(),name='user-info')
    # path('<int:pk>')
]
