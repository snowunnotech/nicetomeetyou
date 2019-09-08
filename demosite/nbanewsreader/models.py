from django.db import models

# Create your models here.

class NewsIndex(models.Model):
    uid = models.CharField(max_length=32, primary_key=True)
    url = models.CharField(max_length=1024)

class NewsDetail(models.Model):
    index = models.ForeignKey('NewsIndex', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    published_at = models.DateTimeField(auto_now=False)
    content = models.TextField()