from django.urls import path,include
from .views import AboutPageView, AllProducts, HomePage,DetailsPage, ProductAdd, ReviewPage,ShopPage,ContactPage,UpdateCart,CartPage,CheckOut

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('post/<int:pk>/', DetailsPage,name='product'),
    path('update_cart/',UpdateCart,name='update_cart'),
    path('orders/',CartPage,name='cart_page'),
    path('checkout/',CheckOut,name='checkOut'),
    path('about/',AboutPageView,name='about'),
    path('shop/',ShopPage.as_view(),name='shop'),
    path('contacts/',ContactPage.as_view(),name='contacts'),
    path('review_page/<int:pk>/',ReviewPage,name='review_page'),
    path('add_product/',ProductAdd.as_view(),name='add_product'),
    path('prod_api/',AllProducts,name='prod_api'),
]
