from rest_framework import viewsets

from . import model, serializer


class UTIViewSet(viewsets.ModelViewSet):
    queryset = model.UTI.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializer.UTIReadSerializer

        return serializer.UTIDefaultSerializer
