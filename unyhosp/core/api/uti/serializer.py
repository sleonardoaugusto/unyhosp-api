from rest_framework import serializers

from . import model

from unyhosp.core.api.bed.serializer import BedDefaultSerializer
from unyhosp.core.api.uti.model import UTI
from .utils import UTIService


class UTIDefaultSerializer(serializers.ModelSerializer,
                           UTIService):
    class Meta:
        model = model.UTI
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        self.apply_service(instance)
        return instance


class UTIReadSerializer(serializers.ModelSerializer):
    beds = BedDefaultSerializer(many=True, read_only=True)

    class Meta:
        model = model.UTI
        fields = (
            'id',
            'name',
            'beds',
            'hospital'
        )
