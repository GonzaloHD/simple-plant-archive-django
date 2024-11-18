# catalog/urls.py

from django.http import HttpResponseRedirect
from django.urls import path
from .api_views import PlantListCreateAPIView, PlantRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/plants/')),
    path('api/plants/', PlantListCreateAPIView.as_view(), name='plant_list_create'),  # List and Create
    path('api/plants/<int:pk>/', PlantRetrieveUpdateDestroyAPIView.as_view(), name='plant_detail_update_delete'),  # Retrieve, Update, Delete
]