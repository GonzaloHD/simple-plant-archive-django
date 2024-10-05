# catalog/serializers.py

from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'image']  # Relevant fields
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True}  # Optional field
        }

        