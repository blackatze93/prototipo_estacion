from django.shortcuts import render
from mediciones.models import Medida
from prototipo_estacion.utils import get_dates
from datetime import datetime
import pytz
import pandas as pd

TZ = pytz.timezone('America/Bogota')
plantilla_presion = 'graficos/presion.html'
plantilla_humedad = 'graficos/humedad.html'
plantilla_temperatura = 'graficos/temperatura.html'
plantilla_co2 = 'graficos/co2.html'

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

            return render(request, plantilla_presion,
                          {'fechas': fechas, 'presiones': presiones, 'dates': request.POST['dates']})

        return render(request, plantilla_presion, {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(TZ).date()).values('fecha',
                                                                             'presion')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        presiones = medidas.values.tolist()

        return render(request, plantilla_presion, {'fechas': fechas, 'presiones': presiones})


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

            return render(request, plantilla_temperatura,
                          {'fechas': fechas, 'temperaturas': temperaturas, 'dates': request.POST['dates']})

        return render(request, plantilla_temperatura, {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(TZ).date()).values('fecha',
                                                                             'temperatura')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        temperaturas = medidas.values.tolist()

        return render(request, plantilla_temperatura, {'fechas': fechas, 'temperaturas': temperaturas})


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

            return render(request, plantilla_humedad,
                          {'fechas': fechas, 'humedades': humedades, 'dates': request.POST['dates']})

        return render(request, plantilla_humedad, {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(TZ).date()).values('fecha',
                                                                             'humedad')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        humedades = medidas.values.tolist()

        return render(request, plantilla_humedad, {'fechas': fechas, 'humedades': humedades})


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

            return render(request, plantilla_co2,
                          {'fechas': fechas, 'co2_ppm': co2_ppm, 'dates': request.POST['dates']})

        return render(request, plantilla_co2, {'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(
            Medida.objects.filter(fecha__gte=datetime.now(TZ).date()).values('fecha',
                                                                             'co2_ppm')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        co2_ppm = medidas.values.tolist()

        return render(request, plantilla_co2, {'fechas': fechas, 'co2_ppm': co2_ppm})
