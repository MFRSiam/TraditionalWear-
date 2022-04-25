from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Products
# Create your views here.

class HomePage(ListView):
    model = Products
    template_name = 'index.html'
    context_object_name = 'all_products'


class DetailsPage(DetailView):
    model = Products
    template_name = 'details.html'
    context_object_name = 'each_product'
    

def AboutPageView(request):
    return render(request,'about.html')
