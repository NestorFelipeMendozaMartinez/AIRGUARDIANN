from django.db import models
from usuarios.models import Usuario

class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sensores')

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
