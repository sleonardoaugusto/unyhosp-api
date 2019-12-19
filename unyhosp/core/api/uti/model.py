from django.db import models
from unyhosp.core.api.hospital.model import Hospital


class UTI(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    hospital = models.ForeignKey(Hospital, related_name='utis', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
