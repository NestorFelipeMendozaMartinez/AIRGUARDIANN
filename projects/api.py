from rest_framework import viewsets
from .models import usuario, Sensor, Lectura, Cortina
from .serializers import usuarioSerializer, SensorSerializer, LecturaSerializer, CortinaSerializer

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class LecturaViewSet(viewsets.ModelViewSet):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer

class CortinaViewSet(viewsets.ModelViewSet):
    queryset = Cortina.objects.all()
    serializer_class = CortinaSerializer
