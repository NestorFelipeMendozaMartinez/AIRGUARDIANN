from django.urls import path
from .views import LecturaListCreate, LecturaDetail

urlpatterns = [
    path('', LecturaListCreate.as_view(), name='lectura-list'),  # <- sin 'lecturas/'
    path('<int:pk>/', LecturaDetail.as_view(), name='lectura-detail'),
]
