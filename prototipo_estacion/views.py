from django.shortcuts import render


def index(request):
    return render(request, 'prototipo_estacion/index.html')


def contacto(request):
    return render(request, 'prototipo_estacion/contacto.html')
