from django.urls import path

from . import views

urlpatterns = [
    path('temperatura/', views.temperatura, name='temperatura')
]
