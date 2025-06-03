from rest_framework import serializers
from .models import usuario , Sensor, Lectura, Cortina

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id', 'nome', 'email', 'rol')  # Include all fields from the model
        read_only_fields = ( 'creat_at', )  # id is automatically generated and should not be modified by the user

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