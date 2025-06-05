# cortinas/serializers.py
from rest_framework import serializers
from .models import Sensor  # Asegúrate de que el modelo esté importado correctamente

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'