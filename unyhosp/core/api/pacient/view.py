from rest_framework import viewsets
from django_filters import rest_framework

from . import model, serializer


class PacientFilter(rest_framework.FilterSet):
    name = rest_framework.filters.CharFilter(lookup_expr='icontains')
    document_id = rest_framework.filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = model.Pacient
        fields = ['name', 'document_id']


class PacientViewSet(viewsets.ModelViewSet):
    queryset = model.Pacient.objects.all()
    serializer_class = serializer.PacientSerializer
    filterset_class = PacientFilter
