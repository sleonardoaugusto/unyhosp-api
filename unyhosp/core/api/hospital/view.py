from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from . import model, serializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = model.Hospital.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializer.HospitalReadSerializer

        return serializer.HospitalDefaultSerializer
