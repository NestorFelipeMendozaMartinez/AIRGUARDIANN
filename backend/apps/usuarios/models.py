from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre