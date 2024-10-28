# catalog/api_views.py

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter
from .models import Plant
from .serializers import PlantSerializer

# List and Create Plants
class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = [MultiPartParser, FormParser]  # Allow file uploads
    filter_backends = [SearchFilter]  # Add search filter
    search_fields = ['name', 'description']  # Search by name and description

# Retrieve, Update, and Delete a Plant
class PlantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = [MultiPartParser, FormParser]  # Allow file uploads and form data