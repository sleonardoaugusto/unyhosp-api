from rest_framework import serializers

from . import model


class PacientSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'])

    class Meta:
        model = model.Pacient
        fields = '__all__'
