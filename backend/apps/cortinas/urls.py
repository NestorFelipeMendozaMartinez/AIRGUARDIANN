from django.urls import path
from .views import CortinaListCreate, CortinaDetail

urlpatterns = [
    path('', CortinaListCreate.as_view(), name='cortina-list'),          # nota el '' vacío
    path('<int:pk>/', CortinaDetail.as_view(), name='cortina-detail'),
]
