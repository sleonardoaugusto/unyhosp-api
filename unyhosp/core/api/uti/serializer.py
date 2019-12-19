from rest_framework import serializers

from . import model

from unyhosp.core.api.bed.serializer import BedDefaultSerializer


class UTIDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.UTI
        fields = '__all__'


class UTIReadSerializer(serializers.ModelSerializer):
    beds = BedDefaultSerializer(many=True, read_only=True)

    class Meta:
        model = model.UTI
        fields = (
            'id',
            'name',
            'beds'
        )
