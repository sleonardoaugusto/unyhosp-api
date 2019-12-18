from rest_framework import viewsets

from . import model, serializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = model.Hospital.objects.all()
    serializer_class = serializer.HospitalSerializer
