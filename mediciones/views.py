from django.shortcuts import render
from mediciones.models import Medida


def index(request):
    medidas = Medida.objects.all()

    return render(request, 'mediciones/index.html', {'medidas': medidas})

# Create your views here.
