from django.db import models


# Create your models here.
class Medida(models.Model):
    """
    Clase que representa el modelo de una medida en la base de datos
    """
    fecha = models.DateTimeField()
    presion = models.FloatField()
    humedad = models.FloatField()
    temperatura = models.FloatField()
    co2_ppm = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()
