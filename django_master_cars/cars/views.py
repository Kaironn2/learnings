from django.shortcuts import render
from django.http import HttpRequest
from cars.models import Car
from cars.forms import CarForm, CarModelForm


def cars_view(request: HttpRequest):
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search)
    else:
        cars = Car.objects.all()
    cars = cars.order_by('model')
    return render(request, 'cars.html', {'cars': cars})


def new_car_view(request: HttpRequest):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car = new_car_form.save()
            new_car.save()
            return render(request, 'new_car.html', {'form': new_car_form, 'success': True})
    elif request.method == 'GET':
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'form': new_car_form})