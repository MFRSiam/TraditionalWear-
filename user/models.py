from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    phoneNumber = models.CharField(max_length=30,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False,) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    is_supplier = models.BooleanField(default=False)
    is_starCustomer = models.BooleanField(default=False)
    is_starSupplier = models.BooleanField(default=False)
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username
    
    
class UserAddressInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    UserId = models.ForeignKey(MyUser,on_delete=models.CASCADE);
    address = models.TextField()
    def __str__(self):
        return self.UserId

