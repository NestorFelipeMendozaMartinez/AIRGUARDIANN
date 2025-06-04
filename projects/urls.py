from django.urls import path
from .views import (
    usuarioListCreateView, usuarioDetailView,
    SensorListCreateView, SensorDetailView,
    LecturaListCreateView, LecturaDetailView,
    CortinaListCreateView, CortinaDetailView
)

urlpatterns = [
    path('usuarios/', usuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', usuarioDetailView.as_view(), name='usuario-detail'),
    
    path('sensores/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensores/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),

    path('lecturas/', LecturaListCreateView.as_view(), name='lectura-list-create'),
    path('lecturas/<int:pk>/', LecturaDetailView.as_view(), name='lectura-detail'),

    path('cortinas/', CortinaListCreateView.as_view(), name='cortina-list-create'),
    path('cortinas/<int:pk>/', CortinaDetailView.as_view(), name='cortina-detail'),
]