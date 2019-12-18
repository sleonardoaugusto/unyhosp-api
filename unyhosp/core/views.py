from rest_framework import viewsets

from . import models, serializers


class BedViewSet(viewsets.ModelViewSet):
    queryset = models.Bed.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.BedReadSerializer

        return serializers.BedActionsSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer
