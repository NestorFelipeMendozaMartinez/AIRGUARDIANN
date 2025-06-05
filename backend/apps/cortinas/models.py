from django.db import models
from sensores.models import Sensor

class Cortina(models.Model):
    estado = models.CharField(max_length=10, choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada')])
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='cortinas')

    def __str__(self):
        return f"Cortina {self.estado} (Sensor: {self.sensor.nombre})"
