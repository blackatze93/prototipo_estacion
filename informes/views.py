import json

from django.shortcuts import render
from mediciones.models import Medida
import pandas as pd
from prototipo_estacion.utils import get_dates
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from requests import Session
from urllib.parse import quote


def informes(request):
    return render(request, 'informes/index.html')


def ver_plantilla(request):
    if request.method == 'POST':
        dates = get_dates(request.POST['dates'].split())

        df = pd.DataFrame(
            list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                          'temperatura')))

        if not df.empty:
            medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

            fechas = medidas.index.to_series().astype(str).values.tolist()
            temperaturas = medidas.values.tolist()

            session = Session()

            options = json.dumps({
                'chart': {
                    'type': 'column'
                },
                'credits': {
                    'enabled': 'false'
                },
                'title': {
                    'text': 'Temperatura promedio por día'
                },
                'xAxis': {
                    'categories': fechas,
                    'crosshair': 'true',
                },
                'yAxis': {
                    'min': 0,
                    'title': {
                        'text': 'Temperatura'
                    }
                },
                'plotOptions': {
                    'column': {
                        'pointPadding': 0.2,
                        'borderWidth': 0
                    }
                },
                'series': [{
                    'name': 'Temperatura',
                    'data': temperaturas,
                }]
            }, separators=(',', ':'))

            data = quote('async=true&type=image/png&width=900&options=' + options, safe='~@#$&()*!+=:;,.?/\'')
            url = "https://export.highcharts.com/"

            response = session.post(url, data=data, headers={'content-type': 'application/x-www-form-urlencoded'})

            img = url + response.text

            print(img)

            return render(request, 'informes/informes.html',
                          {'dates': dates, 'fechas': fechas, 'temperaturas': temperaturas, 'img': img})
        return render(request, 'informes/index.html', {'dates': request.POST['dates']})


def generar_pdf(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template('informes/informes.html')
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return HttpResponse(request, 'informes/informes.html')
