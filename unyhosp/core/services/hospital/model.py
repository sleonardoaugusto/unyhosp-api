from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
