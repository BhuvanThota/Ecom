from django.db import models
import datetime

# Create your models here.

# Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    
# Customer
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, default = '', blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


# Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=1, null=True)
    description = models.TextField(default = '', blank=True, null= True)
    image = models.ImageField(upload_to='uploads/product/')
    # Adding Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default = 0, max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

# order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default = '', blank= True)
    phone = models.CharField(max_length=20, default = '', blank=True)
    date = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
