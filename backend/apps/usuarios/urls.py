from django.urls import path
from .views import UsuariolistCreateview, UsuarioDetailView

urlpatterns = [
    path('', UsuariolistCreateview.as_view(), name='usuario-list-create'),
    path('<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
]