from django.shortcuts import render
from mediciones.models import Medida
from prototipo_estacion.utils import get_dates


def mediciones(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        medidas_filtered = Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date'])

        return render(request, 'mediciones/index.html', {'medidas': medidas_filtered, 'dates': request.POST['dates']})
    else:
        medidas = Medida.objects.all()
        return render(request, 'mediciones/index.html', {'medidas': medidas})
