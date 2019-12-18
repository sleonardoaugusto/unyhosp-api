from rest_framework import serializers

from . import models


class UTISerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UTI
        fields = '__all__'


class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pacient
        fields = '__all__'


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
