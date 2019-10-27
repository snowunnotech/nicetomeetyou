from django.db import models

class news(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField (max_length = 1000)