from rest_framework import serializers

from . import models
from unyhosp.core.pacient.serializer import PacientSerializer


class BedReadSerializer(serializers.ModelSerializer):
    pacient = PacientSerializer(read_only=True)

    class Meta:
        model = models.Bed
        fields = '__all__'


class BedActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bed
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'
