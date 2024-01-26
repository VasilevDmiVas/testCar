from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_car, name='add_car'),
    path('cars/', views.get_cars, name='cars'),
]
