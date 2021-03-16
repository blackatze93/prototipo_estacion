from django.urls import path

from . import views

urlpatterns = [
    path('', views.informes, name='informes'),
    path('ver', views.ver_plantilla, name='ver_plantilla'),
    path('generar', views.generar_pdf, name='generar_pdf'),
]
