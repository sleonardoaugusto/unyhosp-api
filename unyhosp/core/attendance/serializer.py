from rest_framework import serializers

from . import model


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.Attendance
        fields = '__all__'
