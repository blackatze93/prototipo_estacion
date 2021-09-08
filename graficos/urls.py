from django.urls import path

from . import views

urlpatterns = [
    path('presion/', views.presion, name='presion'),
    path('temperatura/', views.temperatura, name='temperatura'),
    path('humedad/', views.humedad, name='humedad'),
    path('co2/', views.co2, name='co2'),
]
