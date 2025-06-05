from rest_framework import generics
from .models import Lectura
from .serializers import LecturaSerializer
from cortinas.models import Cortina
from sensores.models import Sensor  # Necesario para acceder al sensor vinculado

class LecturaListCreateView(generics.ListCreateAPIView):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer

    def perform_create(self, serializer):
        lectura = serializer.save()  # Guarda la lectura y la asigna

        sensor = lectura.sensor  # Accedemos al sensor relacionado con la lectura
        cortinas = sensor.cortinas.all()  # Accedemos a todas las cortinas asociadas

        # Lógica de control automático
        if sensor.tipo == 'temperatura' and lectura.valor > 30:
            for cortina in cortinas:
                cortina.estado = 'abierta'
                cortina.save()
        elif sensor.tipo == 'temperatura' and lectura.valor <= 25:
            for cortina in cortinas:
                cortina.estado = 'cerrada'
                cortina.save()
