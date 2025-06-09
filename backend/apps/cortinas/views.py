from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cortina
from .serializers import CortinaSerializer

class CortinaListCreate(generics.ListCreateAPIView):
    queryset = Cortina.objects.all()
    serializer_class = CortinaSerializer

class CortinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cortina.objects.all()
    serializer_class = CortinaSerializer

    def post(self, request, *args, **kwargs):
        cortina = self.get_object()
        action = request.data.get('action')

        if action == 'abrir':
            cortina.estado = 'abierta'
        elif action == 'cerrar':
            cortina.estado = 'cerrada'
        else:
            return Response({'error': 'Acción no válida'}, status=status.HTTP_400_BAD_REQUEST)

        cortina.save()
        return Response({'status': f'Cortina {cortina.estado}'})