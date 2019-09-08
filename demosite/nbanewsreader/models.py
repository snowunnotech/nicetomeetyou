from django.db import models

# Create your models here.

class News(models.Model):
    uid = models.CharField(max_length=32, primary_key=True)
    url = models.CharField(max_length=1024)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    published_at = models.DateTimeField(auto_now=False)
    content = models.TextField()