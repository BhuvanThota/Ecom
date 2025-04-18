from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["category",]

admin.site.register(Product, ProductAdmin)