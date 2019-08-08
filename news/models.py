from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30, default='')
    time = models.CharField(max_length=20, default='')
    url = models.URLField(default='')
    imgUrl = models.URLField(default='')
    payload = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)


class NewsStory(models.Model):
    parent = models.ForeignKey(News, on_delete=models.CASCADE)
    fbLike = models.CharField(max_length=15, default='')
    author = models.CharField(max_length=50, default='')
    payload = models.TextField(default='')
    imgUrl = models.URLField(default='')
    vedioUrl = models.URLField(default='')
