from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuariolistCreateview(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUptateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
