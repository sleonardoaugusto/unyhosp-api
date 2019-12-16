from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class UTI(models.Model):
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Bed(models.Model):
    name = models.CharField(max_length=255)
    uti = models.ForeignKey(UTI, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Pacient(models.Model):
    name = models.CharField(max_length=255)
    document_id = models.IntegerField()
    email = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


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
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, blank=True)
