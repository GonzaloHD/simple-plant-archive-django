# catalog/models.py

from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # Allow null and blank
    image = models.ImageField(upload_to='plants/', null=True, blank=True)  # Optional image
    buy_price = models.FloatField(null=True, blank=True)  # Allow null for buy price
    sell_price = models.FloatField(null=True, blank=True)  # Allow null for sell price
    stock = models.IntegerField(default=0)  # Default to 0

    def __str__(self):
        return self.name
