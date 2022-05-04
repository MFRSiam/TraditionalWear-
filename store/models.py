from asyncio.windows_events import NULL
from django.db import models
from django.urls import reverse
from user.models import MyUser
import datetime
# Create your models here.




class Products(models.Model):
    Product_TYPES = [("Lungi","Lungi"),("Sharee","Sharee"),("Panjabi","Punjabi")]
    Product_id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(decimal_places=2,max_digits=9)
    Product_Type = models.CharField(choices=Product_TYPES,max_length=25,default="UD")
    Description = models.TextField(max_length=300)
    Brand = models.SlugField(max_length=20)
    ProductImage = models.ImageField(upload_to='images/')
    def __str__(self):
        sid = str(self.Product_id)
        return str(self.Name) + " ID: " + sid
    
    def get_absolute_url(self): # new
        return reverse('product', args=[str(self.Product_id)])


class Orders(models.Model):
    TransactionID =models.CharField(primary_key=True,default='XXX',max_length=50)
    Date = models.DateTimeField(auto_now_add=True)
    Customer_Id = models.ForeignKey(MyUser,on_delete=models.CASCADE,db_constraint=False)
    ProductID = models.ForeignKey(Products,on_delete=models.CASCADE,db_constraint=False,default=NULL)
    # Amount = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.TransactionID

class OrderedProductInfo(models.Model):
    TransactionID = models.ForeignKey(Orders,on_delete=models.CASCADE,db_constraint=False)
    ProductID = models.ForeignKey(Products,on_delete=models.CASCADE,db_constraint=False,default=NULL)
    # def __str__(self) -> str:
    #     return self.ProductID + " " + self.TransactionID
    
class Review(models.Model):
    ProductId = models.ForeignKey(Products,on_delete=models.CASCADE,db_constraint=False)
    CustomerId = models.ForeignKey(MyUser,on_delete=models.CASCADE,db_constraint=False)
    ReviewDate = models.DateTimeField(auto_now_add=True)
    Ratings = models.IntegerField()
    Description = models.TextField(max_length=1000)
    def __str__(self):
        return str(self.ProductId) + " Has " + str(self.Ratings) +" Rating"

class SupplierProductInfo(models.Model):
    SupplierID = models.ForeignKey(MyUser,on_delete=models.CASCADE,db_constraint=False)
    ProductID = models.ForeignKey(Products,on_delete=models.CASCADE,db_constraint=False)
