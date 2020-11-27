from django.shortcuts import render
from django.http import HttpResponse
from mediciones.models import Medida
from datetime import datetime


def index(request):
    if request.method == 'POST':
        dates = request.POST['dates'].split()
        min_date_str = dates[0].split('/')
        max_date_str = dates[2].split('/')

        min_date = datetime(int(min_date_str[2]), int(min_date_str[1]), int(min_date_str[0]))
        max_date = datetime(int(max_date_str[2]), int(max_date_str[1]), int(max_date_str[0]), 23, 59, 59, 999999)

        medidas_filtered = Medida.objects.filter(fecha__gte=min_date, fecha__lte=max_date)

        return render(request, 'mediciones/index.html', {'medidas': medidas_filtered, 'dates': request.POST['dates']})
    else:
        medidas = Medida.objects.all()
        return render(request, 'mediciones/index.html', {'medidas': medidas})
