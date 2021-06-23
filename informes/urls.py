from django.urls import path

from . import views

urlpatterns = [
    path('', views.informes, name='informes'),
    path('generar', views.generar_informe, name='generar_informe'),
]
