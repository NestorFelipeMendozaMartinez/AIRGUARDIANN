from rest_framework import generics
from .models import usuario, Sensor, Lectura, Cortina
from .serializers import usuarioSerializer, SensorSerializer, LecturaSerializer, CortinaSerializer

# Vistas para Usuario
class usuarioListCreateView(generics.ListCreateAPIView):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

class usuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

# Vistas para Sensor
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Vistas para Lectura
class LecturaListCreateView(generics.ListCreateAPIView):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer

class LecturaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer

# Vistas para Cortina
class CortinaListCreateView(generics.ListCreateAPIView):
    queryset = Cortina.objects.all()
    serializer_class = CortinaSerializer

class CortinaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cortina.objects.all()
    serializer_class = CortinaSerializer
