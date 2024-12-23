# catalog/api_views.py

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.filters import SearchFilter

from .permissions import IsAuthenticatedOrReadOnly
from .models import Plant
from .serializers import PlantSerializer

# List and Create Plants
class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]  # Allow file uploads
    filter_backends = [SearchFilter]  # Add search filter
    search_fields = ['name', 'description']  # Search by name and description
    permission_classes = [IsAuthenticatedOrReadOnly]  # Apply custom permission
    
# Retrieve, Update, and Delete a Plant
class PlantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]  # Allow file uploads and form data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Apply custom permission