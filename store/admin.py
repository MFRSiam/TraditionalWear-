from django.contrib import admin
from .models import Products,Orders,Review,OrderedProductInfo,SupplierProductInfo
# Register your models here.

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Review)
admin.site.register(OrderedProductInfo)
admin.site.register(SupplierProductInfo)