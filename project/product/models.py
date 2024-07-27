from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
