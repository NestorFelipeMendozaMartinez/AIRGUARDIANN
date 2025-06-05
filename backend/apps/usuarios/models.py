from django.db import models

class Usuario(models.model):
    nombre = models.charfiel(max_length=100)
    email = models.charfiel(max_length=100)
    rol = models.charfield(max_length=100)

    def __str__(self):
        return self.nombre