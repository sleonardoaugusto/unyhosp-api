from rest_framework import serializers

from . import model

from unyhosp.core.api.uti.serializer import UTIDefaultSerializer


class HospitalDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Hospital
        fields = '__all__'


class HospitalReadSerializer(serializers.ModelSerializer):
    utis = UTIDefaultSerializer(many=True, read_only=True)

    class Meta:
        model = model.Hospital
        fields = (
            'id',
            'name',
            'utis'
        )
