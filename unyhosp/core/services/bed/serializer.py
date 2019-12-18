from rest_framework import serializers
from . import model

from unyhosp.core.services.pacient.serializer import PacientSerializer


class BedReadSerializer(serializers.ModelSerializer):
    pacient = PacientSerializer(read_only=True)

    class Meta:
        model = model.Bed
        fields = '__all__'


class BedActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Bed
        fields = '__all__'
