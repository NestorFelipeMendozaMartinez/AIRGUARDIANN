from django.db import models


class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # 'temperatura' o 'humedad'
    ubicacion = models.CharField(max_length=100)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='sensores')

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.nombre} - {self.valor} - {self.fecha}"

class Cortina(models.Model):
    estado = models.CharField(max_length=10, choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada')])
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='cortinas')

    def __str__(self):
        return f"Cortina {self.estado} (Sensor: {self.sensor.nombre})"
