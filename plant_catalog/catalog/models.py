# catalog/models.py

from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='plants/', null=True, blank=True)  # Allow null values
    buy_price = models.FloatField(null=True)
    sell_price = models.FloatField(null=True)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return self.name
