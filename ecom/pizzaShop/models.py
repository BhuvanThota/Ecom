from django.db import models

# Create your models here.

class Size(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Pizza(models.Model):
    order_id = models.AutoField(primary_key=True)
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topping1} {self.topping2} {self.size}"
    

