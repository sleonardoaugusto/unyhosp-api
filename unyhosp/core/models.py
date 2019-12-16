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
