from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import  usuarioViewSet, SensorViewSet, LecturaViewSet, CortinaViewSet

router = DefaultRouter()
router.register(r'usuario', usuarioViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'lecturas', LecturaViewSet)
router.register(r'cortinas', CortinaViewSet)

urlpatterns = router.urls

