from django.shortcuts import render
from mediciones.models import Medida
from prototipo_estacion.utils import get_dates
from datetime import datetime
import pytz


def mediciones(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        medidas = Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).order_by('-fecha')

        return render(request, 'mediciones/index.html', {'medidas': medidas, 'dates': request.POST['dates']})
    else:
        medidas = Medida.objects.filter(fecha__gte=datetime.now(pytz.timezone('America/Bogota')).date()).order_by('-fecha')
        return render(request, 'mediciones/index.html', {'medidas': medidas})
