from rest_framework import viewsets

from . import models, serializers


class UTIViewSet(viewsets.ModelViewSet):
    queryset = models.UTI.objects.all()
    serializer_class = serializers.UTISerializer


class PacientViewSet(viewsets.ModelViewSet):
    queryset = models.Pacient.objects.all()
    serializer_class = serializers.PacientSerializer


class BedViewSet(viewsets.ModelViewSet):
    queryset = models.Bed.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializers.BedReadSerializer

        return serializers.BedActionsSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer
