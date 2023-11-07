from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    section = models.ForeignKey('Section', null=True, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=30)
