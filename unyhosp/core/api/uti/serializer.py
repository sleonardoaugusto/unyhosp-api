from rest_framework import serializers

from . import model


class UTISerializer(serializers.ModelSerializer):
    class Meta:
        model = model.UTI
        fields = '__all__'
