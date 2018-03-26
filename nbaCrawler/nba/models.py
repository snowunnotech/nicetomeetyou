from django.db import models

# Create your models here.
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    content = models.TextField(max_length=500, blank=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title