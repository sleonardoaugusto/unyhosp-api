from django.db import models
from unyhosp.core.hospital.model import Hospital


class UTI(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
