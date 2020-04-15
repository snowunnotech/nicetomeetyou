from django.db import models


class NbaNews(models.Model):
    url = models.URLField(blank=True)
    image = models.URLField(blank=True)
    title = models.CharField(max_length=50)
    timestamp = models.DateField(auto_now_add=True)
