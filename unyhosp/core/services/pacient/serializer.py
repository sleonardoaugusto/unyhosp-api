from rest_framework import serializers

from . import model


class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Pacient
        fields = '__all__'
