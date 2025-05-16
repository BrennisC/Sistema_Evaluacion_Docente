from rest_framework import serializers
from .models import Comision, MiembroComision


class ComisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comision
        fields = '__all__'

class MiembroComisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroComision
        fields = '__all__'
