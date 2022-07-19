from django.db import models


# Create your models here.
class Student(models.Model):
    productId = models.CharField(max_length=255, blank=True, null=True, default=0)
    customerId = models.IntegerField(blank=True, default=0)
    total = models.IntegerField(blank=True, default=0)
    discount = models.FloatField(blank=True, default=0)
    subTotal = models.FloatField(blank=True, default=0)
    qty = models.CharField(max_length=255, blank=True, null=True, default=0)
