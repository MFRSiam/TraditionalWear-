from django.db import models
from user.models import MyUser
import datetime
# Create your models here.

def TransactionIDgenerator(Products):
    genID = str(int(Products.objects.last().Price) * 10)
    genType = str(Products.objects.last().Product_Type)
    genTime = str(datetime.datetime.now())
    genString = genID + " "+ genTime + " "+ genType
    return genString



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
        return self.Name + " ID: " + sid



class Orders(models.Model):
    TransactionID =models.CharField(primary_key=True,default=TransactionIDgenerator(Products),max_length=50)
    Date = models.DateTimeField(auto_now_add=True)
    Customer_Id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.TransactionID

class OrderedProductInfo(models.Model):
    TransactionID = models.ForeignKey(Orders,on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.ProductID + " " + self.TransactionID
    
class Review(models.Model):
    ProductId = models.ForeignKey(Products,on_delete=models.CASCADE)
    CustomerId = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    ReviewDate = models.DateTimeField(auto_now_add=True)
    Ratings = models.IntegerField()
    Description = models.TextField(max_length=1000)
    def __str__(self):
        return self.ProductId + " Has " + self.Ratings +" Rating"

class SupplierProductInfo(models.Model):
    SupplierID = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products,on_delete=models.CASCADE)
