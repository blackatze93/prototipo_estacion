from django.shortcuts import render
from mediciones.models import Medida
from datetime import datetime
import pandas as pd


def get_dates(dates_input):
    dates = dict()

    ''' min_date definition '''
    min_date_str = dates_input[0].split('/')
    min_date_day = int(min_date_str[0])
    min_date_month = int(min_date_str[1])
    min_date_year = int(min_date_str[2])
    dates['min_date'] = datetime(min_date_year, min_date_month, min_date_day)
    ''' max_date definition '''
    max_date_str = dates_input[2].split('/')
    max_date_day = int(max_date_str[0])
    max_date_month = int(max_date_str[1])
    max_date_year = int(max_date_str[2])
    dates['max_date'] = datetime(max_date_year, max_date_month, max_date_day, 23, 59, 59, 999999)

    return dates


def presion(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        df = pd.DataFrame(
            list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                          'presion')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        presiones = medidas.values.tolist()

        return render(request, 'graficos/presion.html',
                      {'fechas': fechas, 'presiones': presiones, 'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(Medida.objects.all().values('fecha', 'presion')))

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

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        temperaturas = medidas.values.tolist()

        return render(request, 'graficos/temperatura.html',
                      {'fechas': fechas, 'temperaturas': temperaturas, 'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(Medida.objects.all().values('fecha', 'temperatura')))

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

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        humedades = medidas.values.tolist()

        return render(request, 'graficos/humedad.html',
                      {'fechas': fechas, 'humedades': humedades, 'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(Medida.objects.all().values('fecha', 'humedad')))

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

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        co2_ppm = medidas.values.tolist()

        return render(request, 'graficos/co2.html',
                      {'fechas': fechas, 'co2_ppm': co2_ppm, 'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(Medida.objects.all().values('fecha', 'co2_ppm')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        co2_ppm = medidas.values.tolist()

        return render(request, 'graficos/co2.html', {'fechas': fechas, 'co2_ppm': co2_ppm})
