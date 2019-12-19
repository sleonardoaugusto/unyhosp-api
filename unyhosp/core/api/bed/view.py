from rest_framework import viewsets

from . import model, serializer


class BedViewSet(viewsets.ModelViewSet):
    queryset = model.Bed.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializer.BedReadSerializer

        return serializer.BedDefaultSerializer
