from django.db import models

# Create your models here.
class NbaNews(models.Model):
    uid = models.CharField(unique=True, max_length=100)
    image_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_datetime = models.DateTimeField(null=True, default=None)