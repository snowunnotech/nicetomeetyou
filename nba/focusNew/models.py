from django.db import models

# Create your models here.
class FocusNew(models.Model):
    title = models.CharField(max_length=100)
    post_time = models.CharField(max_length=30)
    writer = models.CharField(max_length=30)
    img_src = models.URLField(blank=True)
    content = models.TextField(blank=True)


