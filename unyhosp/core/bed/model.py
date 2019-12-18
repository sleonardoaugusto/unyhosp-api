from django.db import models
from unyhosp.core.uti.model import UTI
from unyhosp.core.pacient.model import Pacient


class Bed(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    uti = models.ForeignKey(UTI, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
