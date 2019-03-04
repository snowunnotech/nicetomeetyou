from django.db import models

# Create your models here.

class NBAnews(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    