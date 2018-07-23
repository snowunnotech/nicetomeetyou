from django.db import models

class News(models.Model):
    author = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=250, blank=True, default="")
    story_url = models.CharField(max_length=250)
    content = models.TextField()
    video_url = models.CharField(max_length=250, blank=True, default="")

    class Meta:
        unique_together = (("datetime", "title"),)