from django.contrib import admin  # ¡Falta esta importación!
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Ahora 'admin' está definido
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/sensores/', include('apps.sensores.urls')),
    path('api/lecturas/', include('apps.lecturas.urls')),
    path('api/cortinas/', include('apps.cortinas.urls')),
    path('', RedirectView.as_view(url='/api/sensores/')),  # Corregido: sin espacios en el método
]