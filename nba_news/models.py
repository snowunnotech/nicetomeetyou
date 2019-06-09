from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    img = models.CharField(max_length=210, null=True)
    article = models.TextField(default="")
    video = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)