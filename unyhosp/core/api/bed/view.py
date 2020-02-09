from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from . import model, serializer


class BedViewSet(viewsets.ModelViewSet):
    queryset = model.Bed.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializer.BedReadSerializer

        return serializer.BedDefaultSerializer
