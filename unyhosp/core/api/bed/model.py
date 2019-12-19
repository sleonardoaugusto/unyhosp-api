from django.db import models
from unyhosp.core.api.uti.model import UTI
from unyhosp.core.api.pacient.model import Pacient


class Bed(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    uti = models.ForeignKey(UTI, related_name='beds', on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
