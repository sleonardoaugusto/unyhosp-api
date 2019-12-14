from rest_framework import serializers

from . import models


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = '__all__'


class UTISerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UTI
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bed
        fields = '__all__'
