from django.db import models
from apps.sensores.models import Sensor

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.nombre} - {self.valor} - {self.fecha}"
