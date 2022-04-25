from django.urls import path,include
from .views import HomePage,DetailsPage,AboutPageView

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('post/<int:pk>/', DetailsPage.as_view(),name='product'),
    path('about/',AboutPageView,name='about'),
]
