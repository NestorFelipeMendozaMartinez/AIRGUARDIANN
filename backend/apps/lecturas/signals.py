from django.db.models.signals import post_save
from django.dispatch import receiver
from lecturas.models import Lectura
from cortinas.models import Cortina

@receiver(post_save, sender=Lectura)
def manejar_alerta(sender, instance, **kwargs):
    if instance.valor > 30:  # Si temperatura > 30, cerrar cortinas
        Cortina.objects.filter(invernadero=instance.sensor.ubicacion).update(estado='cerrada')