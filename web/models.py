from django.db import models

class news(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 256)