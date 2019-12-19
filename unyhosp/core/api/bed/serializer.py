from rest_framework import serializers
from . import model

from unyhosp.core.api.pacient.serializer import PacientSerializer


class BedDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Bed
        fields = '__all__'


class BedReadSerializer(serializers.ModelSerializer):
    pacient = PacientSerializer(read_only=True)

    class Meta:
        model = model.Bed
        fields = '__all__'
