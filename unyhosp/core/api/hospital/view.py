from rest_framework import viewsets

from . import model, serializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = model.Hospital.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return serializer.HospitalReadSerializer

        return serializer.HospitalActionsSerializer
