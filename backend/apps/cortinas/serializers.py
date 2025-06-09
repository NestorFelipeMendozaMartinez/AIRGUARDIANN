from rest_framework import serializers
from .models import Cortina

class CortinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cortina
        fields = '__all__'