from django.db import models

# Create your models here.

class News(models.Model):
        title = models.CharField(max_length = 30)
        content = models.TextField(blank=True)
        page_url = models.TextField(blank=True)
        img_url = models.URLField(blank=True)
