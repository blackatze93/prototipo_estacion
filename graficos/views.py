from django.shortcuts import render
from mediciones.models import Medida
from datetime import datetime, timedelta
import pandas as pd


def graficos(request):
    if request.method == 'POST':
        dates = request.POST['dates'].split()
        ''' min_date definition '''
        min_date_str = dates[0].split('/')
        min_date_day = int(min_date_str[0])
        min_date_month = int(min_date_str[1])
        min_date_year = int(min_date_str[2])
        min_date = datetime(min_date_year, min_date_month, min_date_day)
        ''' max_date definition '''
        max_date_str = dates[2].split('/')
        max_date_day = int(max_date_str[0])
        max_date_month = int(max_date_str[1])
        max_date_year = int(max_date_str[2])
        max_date = datetime(max_date_year, max_date_month, max_date_day, 23, 59, 59, 999999)

        df = pd.DataFrame(list(Medida.objects.filter(fecha__gte=min_date, fecha__lte=max_date).values('fecha', 'temperatura')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        temperaturas = medidas.values.tolist()

        return render(request, 'graficos/index.html', {'fechas': fechas, 'temperaturas': temperaturas, 'dates': request.POST['dates']})
    else:
        df = pd.DataFrame(list(Medida.objects.all().values('fecha', 'temperatura')))

        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        temperaturas = medidas.values.tolist()

        return render(request, 'graficos/index.html', {'fechas': fechas, 'temperaturas': temperaturas})
