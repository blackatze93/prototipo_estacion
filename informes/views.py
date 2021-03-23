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


def get_img_temperatura(dates):
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
                'text': ''
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
                    'borderWidth': 0,
                    'color': '#717EC3',
                    'dataLabels': {
                        'enabled': 'true',
                        'format': '{point.y:.2f} °C'
                    }
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

        return url + response.text


def get_img_humedad(dates):
    df = pd.DataFrame(
        list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                      'humedad')))

    if not df.empty:
        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        humedades = medidas.values.tolist()

        session = Session()

        options = json.dumps({
            'chart': {
                'type': 'column'
            },
            'credits': {
                'text': ''
            },
            'title': {
                'text': 'Humedad promedio por día'
            },
            'xAxis': {
                'categories': fechas,
                'crosshair': 'true',
            },
            'yAxis': {
                'min': 0,
                'title': {
                    'text': 'Humedad'
                }
            },
            'plotOptions': {
                'column': {
                    'pointPadding': 0.2,
                    'borderWidth': 0,
                    'color': '#AE8799',
                    'dataLabels': {
                        'enabled': 'true',
                        'format': '{point.y:.2f} %'
                    }
                }
            },
            'series': [{
                'name': 'Humedad',
                'data': humedades,
            }]
        }, separators=(',', ':'))

        data = quote('async=true&type=image/png&width=900&options=' + options, safe='~@#$&()*!+=:;,.?/\'')
        url = "https://export.highcharts.com/"

        response = session.post(url, data=data, headers={'content-type': 'application/x-www-form-urlencoded'})

        return url + response.text


def get_img_presion(dates):
    df = pd.DataFrame(
        list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                      'presion')))
    if not df.empty:
        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        presiones = medidas.values.tolist()

        session = Session()

        options = json.dumps({
            'chart': {
                'type': 'column'
            },
            'credits': {
                'text': ''
            },
            'title': {
                'text': 'Presión promedio por día'
            },
            'xAxis': {
                'categories': fechas,
                'crosshair': 'true',
            },
            'yAxis': {
                'min': 0,
                'title': {
                    'text': 'Presión'
                }
            },
            'plotOptions': {
                'column': {
                    'pointPadding': 0.2,
                    'borderWidth': 0,
                    'color': '#C95D63',
                    'dataLabels': {
                        'enabled': 'true',
                        'format': '{point.y:.2f} hPa'
                    }
                }
            },
            'series': [{
                'name': 'Presión',
                'data': presiones,
            }]
        }, separators=(',', ':'))

        data = quote('async=true&type=image/png&width=900&options=' + options, safe='~@#$&()*!+=:;,.?/\'')
        url = "https://export.highcharts.com/"

        response = session.post(url, data=data, headers={'content-type': 'application/x-www-form-urlencoded'})

        return url + response.text


def get_img_co2(dates):
    df = pd.DataFrame(
        list(Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date']).values('fecha',
                                                                                                      'co2_ppm')))

    if not df.empty:
        medidas = df.resample('D', on='fecha').mean().to_period().fillna('null')

        fechas = medidas.index.to_series().astype(str).values.tolist()
        co2_ppm = medidas.values.tolist()

        session = Session()

        options = json.dumps({
            'chart': {
                'type': 'column'
            },
            'credits': {
                'text': ''
            },
            'title': {
                'text': 'CO2 promedio por día'
            },
            'xAxis': {
                'categories': fechas,
                'crosshair': 'true',
            },
            'yAxis': {
                'min': 0,
                'title': {
                    'text': 'CO2'
                }
            },
            'plotOptions': {
                'column': {
                    'pointPadding': 0.2,
                    'borderWidth': 0,
                    'color': '#EE8434',
                    'dataLabels': {
                        'enabled': 'true',
                        'format': '{point.y:.2f} PPM'
                    }
                }
            },
            'series': [{
                'name': 'CO2',
                'data': co2_ppm,
            }]
        }, separators=(',', ':'))

        data = quote('async=true&type=image/png&width=900&options=' + options, safe='~@#$&()*!+=:;,.?/\'')
        url = "https://export.highcharts.com/"

        response = session.post(url, data=data, headers={'content-type': 'application/x-www-form-urlencoded'})

        return url + response.text


def generar_pdf(request):
    template_path = 'informes/informes.html'

    dates = get_dates(request.POST['dates'].split())

    medidas_filtered = Medida.objects.filter(fecha__gte=dates['min_date'], fecha__lte=dates['max_date'])

    img_temperatura = get_img_temperatura(dates)
    img_humedad = get_img_humedad(dates)
    img_presion = get_img_presion(dates)
    img_co2 = get_img_co2(dates)

    context = {'dates': dates, 'img_temperatura': img_temperatura, 'img_humedad': img_humedad,
               'img_presion': img_presion, 'img_co2': img_co2, 'medidas': medidas_filtered}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informe.pdf"'
    # response['Content-Disposition'] = 'inline'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # Check if dataframe is empty
    if img_temperatura is None:
        return render(request, 'informes/index.html', {'dates': request.POST['dates']})

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return HttpResponse(request, 'informes/informes.html')
