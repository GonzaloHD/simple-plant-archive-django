# from django.shortcuts import render, get_object_or_404
# from .models import Plant

# def plant_list(request):
#     plants = Plant.objects.all()
#     return render(request, 'catalog/plant_list.html', {'plants': plants})

# def plant_detail(request, pk):
#     plant = get_object_or_404(Plant, pk=pk)
#     return render(request, 'catalog/plant_detail.html', {'plant': plant})


# from django.views.generic import ListView, DetailView
# from catalog.models import Plant

# class PlantListView(ListView):
#     model = Plant
#     template_name = 'catalog/plant_list.html'  # You should have a corresponding template

# class PlantDetailView(DetailView):
#     model = Plant
#     template_name = 'catalog/plant_detail.html'  # You should have a corresponding template

