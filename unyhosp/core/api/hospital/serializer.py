from rest_framework import serializers

from . import model

from unyhosp.core.api.uti.serializer import UTISerializer


class HospitalActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Hospital
        fields = '__all__'


class HospitalReadSerializer(serializers.ModelSerializer):
    utis = UTISerializer(many=True)

    class Meta:
        model = model.Hospital
        fields = (
            'id',
            'name',
            'utis'
        )
