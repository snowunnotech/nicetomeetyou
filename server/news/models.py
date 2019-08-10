from django.db import models

# Create your models here.
class hotNews(models.Model):
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=500)
    context = models.CharField(max_length=10000)