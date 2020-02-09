from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from django_filters import rest_framework

from . import model, serializer


class UTIFilter(rest_framework.FilterSet):
    hospital = rest_framework.filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = model.UTI
        fields = ['hospital_id']


class UTIViewSet(viewsets.ModelViewSet):
    queryset = model.UTI.objects.all()
    filterset_class = UTIFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializer.UTIReadSerializer

        return serializer.UTIDefaultSerializer
