from django.db import models

class authors (models.Model):
    author_id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=2, blank=True)
    birthDate = models.DateField(blank=True)