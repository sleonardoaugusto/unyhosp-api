from django.db import models


class Pacient(models.Model):
    name = models.CharField(max_length=255)
    document_id = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
