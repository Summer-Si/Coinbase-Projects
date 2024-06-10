from django.db import models

# Create your models here.
class Product(models.Model):
   ticker = models.CharField(max_length=10)
   name = models.CharField(max_length=100)

class Historical(models.Model):
   # one to many relationship: 
   # Cascase: when a Product record is deleted, 
   # all the associated Historical records will also be deleted automatically.
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   timestamp = models.DateTimeField()
   open = models.DecimalField(max_digits=10, decimal_places=2)
   high = models.DecimalField(max_digits=10, decimal_places=2)
   low = models.DecimalField(max_digits=10, decimal_places=2)
   close = models.DecimalField(max_digits=10, decimal_places=2)
   volume = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
   # add volume 
