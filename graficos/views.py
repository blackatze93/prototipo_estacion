from django.shortcuts import render
from mediciones.models import Medida
from prototipo_estacion.utils import get_dates
from datetime import datetime
import pytz
import pandas as pd


def presion(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        df = pd.DataFrame(
            list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                          'presion')))
        if not df.empty:
            medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

            fechas = medidas.index.to_series().astype(str).values.tolist()
            presiones = medidas.values.tolist()

            return render(request, 'graficos/presion.html',
                          {'fechas': fechas, 'presiones': presiones, 'dates': request.POST['dates']})

        return render(request, 'graficos/presion.html', {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(pytz.timezone('America/Bogota')).date()).values('fecha',
                                                                                                          'presion')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        presiones = medidas.values.tolist()

        return render(request, 'graficos/presion.html', {'fechas': fechas, 'presiones': presiones})


def temperatura(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        df = pd.DataFrame(
            list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                          'temperatura')))
        if not df.empty:
            medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

            fechas = medidas.index.to_series().astype(str).values.tolist()
            temperaturas = medidas.values.tolist()

            return render(request, 'graficos/temperatura.html',
                          {'fechas': fechas, 'temperaturas': temperaturas, 'dates': request.POST['dates']})

        return render(request, 'graficos/temperatura.html', {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(pytz.timezone('America/Bogota')).date()).values('fecha',
                                                                                                          'temperatura')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        temperaturas = medidas.values.tolist()

        return render(request, 'graficos/temperatura.html', {'fechas': fechas, 'temperaturas': temperaturas})


def humedad(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        df = pd.DataFrame(
            list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                          'humedad')))

        if not df.empty:
            medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

            fechas = medidas.index.to_series().astype(str).values.tolist()
            humedades = medidas.values.tolist()

            return render(request, 'graficos/humedad.html',
                          {'fechas': fechas, 'humedades': humedades, 'dates': request.POST['dates']})

        return render(request, 'graficos/humedad.html', {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(pytz.timezone('America/Bogota')).date()).values('fecha',
                                                                                                          'humedad')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        humedades = medidas.values.tolist()

        return render(request, 'graficos/humedad.html', {'fechas': fechas, 'humedades': humedades})


def co2(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        df = pd.DataFrame(
            list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                          'co2_ppm')))

        if not df.empty:
            medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

            fechas = medidas.index.to_series().astype(str).values.tolist()
            co2_ppm = medidas.values.tolist()

            return render(request, 'graficos/co2.html',
                          {'fechas': fechas, 'co2_ppm': co2_ppm, 'dates': request.POST['dates']})

        return render(request, 'graficos/co2.html', {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(pytz.timezone('America/Bogota')).date()).values('fecha',
                                                                                                          'co2_ppm')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        co2_ppm = medidas.values.tolist()

        return render(request, 'graficos/co2.html', {'fechas': fechas, 'co2_ppm': co2_ppm})
