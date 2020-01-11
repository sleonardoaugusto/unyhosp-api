from django.db import models
from unyhosp.core.api.hospital.model import Hospital
from unyhosp.core.api.pacient.model import Pacient


class Attendance(models.Model):
    entry_reason = models.TextField(null=True)
    hma = models.TextField(null=True)
    comorbidity = models.TextField(null=True)
    atb = models.TextField(null=True)
    hd = models.TextField(null=True)
    medicines_in_use = models.TextField(null=True)
    previous_pathologies = models.TextField(null=True)
    allergies = models.TextField(null=True)
    cultures = models.TextField(null=True)
    vasoactive_drugs = models.TextField(null=True)
    sedation = models.TextField(null=True)
    venous_access = models.TextField(null=True)
    diet = models.TextField(null=True)
    probes_and_drains = models.TextField(null=True)
    ventilation = models.TextField(null=True)
    complications = models.TextField(null=True)
    therapeutic_plan = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
