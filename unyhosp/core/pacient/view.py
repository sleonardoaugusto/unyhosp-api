from rest_framework import viewsets

from . import model, serializer


class PacientViewSet(viewsets.ModelViewSet):
    queryset = model.Pacient.objects.all()
    serializer_class = serializer.PacientSerializer
