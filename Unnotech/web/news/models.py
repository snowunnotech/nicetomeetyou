from django.db import models

# Create your models here.
class News(models.Model):
    article_id = models.PositiveIntegerField(unique=True)
    author = models.CharField(max_length=100, blank=True, default='')
    datetime = models.DateTimeField()
    title = models.CharField(max_length=100, blank=True, default='')
    image_url = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    url = models.CharField(max_length=100, blank=True, default='')
