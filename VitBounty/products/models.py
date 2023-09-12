from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    

class Offer(models.Model):
    code = models.CharField(max_length=10, default='GIFT100')
    description = models.CharField(max_length=255, default='100 ₺ discount for all products !')
    discount = models.FloatField()
