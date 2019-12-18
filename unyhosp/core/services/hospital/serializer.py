from rest_framework import serializers

from . import model


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Hospital
        fields = '__all__'
