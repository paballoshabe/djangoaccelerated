from django.db import models
 
# Create your models here.
 
class Product(models.Model):
 
    #Charfield is equal to varchar
 
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128,unique=True,null=False)
    product_brand = models.CharField(max_length=100,unique=True,null=False)
    product_color = models.CharField(max_length=50,unique=True,null=False)
    product_quantity = models.IntegerField()
    product_size = models.IntegerField(null=False)
 
 
    def __str__(self):
 
        return self.product_name
 
 
class Customer(models.Model):
 
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    name = models.CharField(max_length=128,null=False)
    contact_num  = models.CharField(max_length=20)
    email  = models.EmailField(unique=True,null=False)
    address = models.CharField(max_length=128,null=False)
 
 
    def __str__(self):
 
        return self.name
 
