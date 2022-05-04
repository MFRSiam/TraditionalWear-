import datetime
import io
from venv import create
from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, JsonResponse,FileResponse
from .models import Products,Orders,OrderedProductInfo,Review,SupplierProductInfo
import json
from .forms import ReviewFrom, ProductAddFrom
from reportlab.pdfgen import canvas
# Create your views here.

class HomePage(ListView):
    model = Products
    template_name = 'index.html'
    context_object_name = 'all_products'


# class DetailsPage(DetailView):
#     model = Products
#     template_name = 'details.html'
#     context_object_name = 'each_product'


def DetailsPage(request,pk):
    product = Products.objects.get(Product_id=pk)
    review = Review.objects.filter(ProductId=product)
    return render(request,'details.html',{'product':product,'review':review})


def AboutPageView(request):
    return render(request,'about.html')


class ShopPage(ListView):
    model = Products
    template_name = 'shop.html'
    context_object_name = 'all_products'


def AllProducts(request):
    prod = Products.objects.all().values()
    return JsonResponse({'prod':list(prod)},safe=False)


class ContactPage(TemplateView):
    template_name = 'contact.html'


def UpdateCart(request):
    data =json.loads(request.body)
    action = data['action']
    if action == 'add':
        productId = data['productId']
        # print("Action" ,action , " ProductID: ", productId)

        user = request.user
        product = Products.objects.get(Product_id=productId)
        
        # order,create = order.objects.get_or_create(TransactionI = transactionid(product.Name,product.Product_Type),Customer_Id = user)
        x = Orders(TransactionID = transactionid(product.Name,product.Product_Type),Customer_Id = user,ProductID=product)
        x.save()
        # y = OrderedProductInfo(TransactionID=x,ProductID=product)
        # y.save()
        return JsonResponse('Data Was Added',safe=False)
    elif action == 'remove':
        orderId = data['orderId']
        user = request.user
        Orders.objects.filter(TransactionID=orderId).delete()
        return JsonResponse('Data Was Deleted Successfully',safe=False)



def transactionid(productname,producttype):
    genTime = str(datetime.datetime.now())
    genString = productname + "-"+ genTime + "-"+ producttype
    return genString


def CartPage(request):
    user = request.user
    price =0
    orders = Orders.objects.all()
    user = request.user
    for order in orders:
        if(order.Customer_Id.id == user.id): 
            price += int(order.ProductID.Price)
    
    # orderedProduct = OrderedProductInfo.objects.all()
    return render(request,'orders.html',{"orders": orders, "price":price})

def ReviewPage(request,pk):
    user = request.user
    if request.method == 'POST':
        review_from = ReviewFrom(request.POST)
        if review_from.is_valid():
            y = '/post/' + str(pk) + '/'
            data = review_from.data
            review = data['Review']
            description = data['Description']
            product = Products.objects.get(Product_id=pk)
            new_Review = Review(ProductId=product,CustomerId=user,Ratings=review,Description = description)
            new_Review.save()
            return HttpResponseRedirect(y)    

        else:
            context = {
                'review_from': review_from,
            }
    else:
        context = {
            'review_from': ReviewFrom(),
        }
        
    return render(request,'add_review.html',context)



def ProductAddPage(request):
    user = request.user
    if request.method == 'POST':
        product_add_form = ProductAddFrom(request.POST,request.FILES)

        if product_add_form.is_valid():
            # data = product_add_form.data
            # Name = data['Name']
            # Price = data['Price']
            # Product_Type = data['Product_Type']
            # Description = data['Description']
            # Brand = data['Brand']
            # ProductImage = data['ProductImage']
            # newProduct = Products(Name=Name,Price=Price,Product_Type=Product_Type,Description=Description,Brand=Brand,ProductImage=ProductImage)
            # newProduct.save()
            product_add_form.save()
            return HttpResponseRedirect('')    

        else:
            context = {
                'review_from': product_add_form
            }
    else:
        context = {
            'review_from': ProductAddFrom()
        }
        
    return render(request,'addProduct.html',context)

class ProductAdd(CreateView):
    model = Products
    template_name = 'addProduct.html'
    fields = ['Name', 'Price','Product_Type','ProductImage','Description','Brand']


def CheckOut(request):
    user = request.user
    orders = Orders.objects.filter(Customer_Id = user)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    i=50
    j=700
    total = 0
    for order in orders:
        p.drawString(i, j-10, str(order.TransactionID))
        p.drawString(i+10, j-70, str(order.Date))
        p.drawString(i+40, j-90, str(order.ProductID.Price))
        total += int(order.ProductID.Price)
        j = j-90
        order.ProductID.delete()
    p.drawString(i+40, j-90, str(total))
    p.showPage()
    p.save()
    buffer.seek(0)
    Orders.objects.filter(Customer_Id=user).delete()
    return FileResponse(buffer, as_attachment=True, filename='invoice.pdf')