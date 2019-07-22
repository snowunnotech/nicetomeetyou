from django.db import models

# Create your models here.
class NBA(models.Model):
    title = models.TextField()
    date_time = models.CharField(max_length=16)
    author = models.TextField()
    content = models.TextField()
    image_source = models.URLField(null=True)
    video_source = models.URLField(null=True)
    article_url = models.URLField(unique=True)
    

