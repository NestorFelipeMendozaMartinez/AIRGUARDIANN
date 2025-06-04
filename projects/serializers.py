from rest_framework import serializers
from .models import usuario, Sensor, Lectura, Cortina

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class LecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectura
        fields = '__all__'

class CortinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cortina
        fields = '__all__'
