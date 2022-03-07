from django.db import models
from apps.author.models import authors

class books (models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=2)
    author = models.ForeignKey(authors, null=False, blank=False, on_delete=models.CASCADE)