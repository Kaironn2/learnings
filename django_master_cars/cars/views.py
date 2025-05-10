from django.shortcuts import render
from django.http import HttpRequest
from cars.models import Car
from cars.forms import CarForm, CarModelForm
from django.views import View
from django.views.generic import ListView
from django.shortcuts import redirect


class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    ordering = ['-model']

    def get_queryset(self):
        cars = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarView(View):
    def get(self, request: HttpRequest):
        new_car_form = CarModelForm()
        return render(
            request, 
            'new_car.html', 
            {'form': new_car_form}
        )
    
    def post(self, request: HttpRequest):
        new_car_form = CarModelForm(request.POST, request.FILES)
        
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        
        return render(
            request, 
            'new_car.html', 
            {'form': new_car_form, 'error': True}
        )
