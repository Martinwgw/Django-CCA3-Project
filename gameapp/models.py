from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
