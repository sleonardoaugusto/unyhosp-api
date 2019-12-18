from rest_framework import viewsets

from . import model, serializer


class UTIViewSet(viewsets.ModelViewSet):
    queryset = model.UTI.objects.all()
    serializer_class = serializer.UTISerializer
