import datetime
from venv import create
from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from django.http import JsonResponse
from .models import Products,Orders,OrderedProductInfo,Review,SupplierProductInfo
import json
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


class ShopPage(ListView):
    model = Products
    template_name = 'shop.html'
    context_object_name = 'all_products'
    

class ContactPage(TemplateView):
    template_name = 'contact.html'


def UpdateCart(request):
    data =json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print("Action" ,action , " ProductID: ", productId)

    user = request.user
    product = Products.objects.get(Product_id=productId)
    
    # order,create = order.objects.get_or_create(TransactionI = transactionid(product.Name,product.Product_Type),Customer_Id = user)
    x = Orders(TransactionID = transactionid(product.Name,product.Product_Type),Customer_Id = user)
    x.save()
    y = OrderedProductInfo(TransactionID=x,ProductID=product)
    y.save()
    return JsonResponse('Data Was Added',safe=False)


def transactionid(productname,producttype):
    genTime = str(datetime.datetime.now())
    genString = productname + "-"+ genTime + "-"+ producttype
    return genString


def CartPage(request):
    user = request.user
    count =0
    orders = Orders.objects.all()
    orderedProduct = OrderedProductInfo.objects.all()
    return render(request,'orders.html',{"orders": orders,"orderedProduct":orderedProduct, "count":count})