from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    return render(request, 'prototipo_estacion/index.html')


@require_GET
def contacto(request):
    return render(request, 'prototipo_estacion/contacto.html')
