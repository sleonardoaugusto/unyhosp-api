from django.db import models
from unyhosp.core.bed.model import Bed


class Attendance(models.Model):
    entry_reason = models.TextField()
    hma = models.TextField()
    comorbidity = models.TextField()
    atb = models.TextField()
    hd = models.TextField()
    medicines_in_use = models.TextField()
    previous_pathologies = models.TextField()
    allergies = models.TextField()
    cultures = models.TextField()
    vasoactive_drugs = models.TextField()
    sedation = models.TextField()
    venous_access = models.TextField()
    diet = models.TextField()
    probes_and_drains = models.TextField()
    ventilation = models.TextField()
    complications = models.TextField()
    therapeutic_plan = models.TextField()
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, blank=True)
