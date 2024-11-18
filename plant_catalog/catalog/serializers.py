# catalog/serializers.py

from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'image', 'buy_price', 'sell_price', 'stock']  # Include all fields
        extra_kwargs = {
            'buy_price': {'required': False, 'allow_null': True},  # Allow null for buy price
            'sell_price': {'required': False, 'allow_null': True},  # Allow null for sell price
            'image': {'required': False, 'allow_null': True},  # Allow image to be optional
            'description': {'required': False, 'allow_null': True},  # Optional description
        }

        