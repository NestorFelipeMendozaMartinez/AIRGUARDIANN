from rest_framework import generics
from .models import Lectura
from .serializers import LecturaSerializer

class LecturaListCreate(generics.ListCreateAPIView):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer

class LecturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer