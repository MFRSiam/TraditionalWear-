from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    phoneNumber = models.CharField(max_length=30,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False,) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username
    
    
class CustomerAddresInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    customerID = models.ForeignKey(Customer,on_delete=models.CASCADE);
    address = models.TextField()
    def __str__(self):
        return self.customerID

class Supplier(AbstractUser):
    address = models.TextField(max_length=200)
    phoneNo = models.CharField(max_length=20)
    staff = models.BooleanField(default=False,) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    groups = None
    user_permissions = None
    
    def __str__(self):
        return self.username
