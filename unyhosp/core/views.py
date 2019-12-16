from rest_framework import viewsets

from . import models, serializers


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class UTIViewSet(viewsets.ModelViewSet):
    queryset = models.UTI.objects.all()
    serializer_class = serializers.UTISerializer


class BedViewSet(viewsets.ModelViewSet):
    queryset = models.Bed.objects.all()
    serializer_class = serializers.BedSerializer


class PacientViewSet(viewsets.ModelViewSet):
    queryset = models.Pacient.objects.all()
    serializer_class = serializers.PacientSerializer
