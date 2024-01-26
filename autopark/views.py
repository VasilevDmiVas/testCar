from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def add_car(request):
    try:
        car_types = [
            CarType(name='Sedan'),
            CarType(name='Truck'),
            CarType(name='SUV'),
        ]
        car_brands = [
            CarBrand(name='BMW'),
            CarBrand(name='Mercedes'),
            CarBrand(name='Audi'),
        ]
        for car_type in car_types:
            car_type.save()
        for car_brand in car_brands:
            car_brand.save()

        for i in range(1, 11):
            car = Car(car_number=f'AA{i}BB{i}', car_type=car_types[0], car_brand=car_brands[0], is_electric=False,
                      year=2000)
            car.save()

        parks = [
            Parking(name='Park 1', address='Address 1', phone_number='123-456-7890', price=10.0,
                    description='Description 1'),
            Parking(name='Park 2', address='Address 2', phone_number='123-456-5566', price=20.0,
                    description='Description 2'),
        ]
        for park in parks:
            park.save()

        parks_slots = [
            ParkingSlot(is_free=True, number=1),
            ParkingSlot(is_free=True, number=2),
            ParkingSlot(is_free=True, number=3),
            ParkingSlot(is_free=True, number=4),
        ]
        for park_slot in parks_slots:
            park_slot.save()

        return HttpResponse('Car added')
    except:
        return HttpResponse('Car not added')

def get_cars(request):
    cars = Car.objects.all()
    return render(request, 'autopark/cars.html', {'cars': cars})