from rest_framework import viewsets

from . import model, serializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = model.Attendance.objects.all()
    serializer_class = serializer.AttendanceSerializer
