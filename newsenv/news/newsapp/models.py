# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class News(models.Model):

    news_title = models.CharField(max_length=200,null=True)
    news_link = models.TextField(max_length=5000,null=True)
    news_content = models.TextField(max_length=5000,null=True)
    news_img = models.TextField(max_length=200,null=True)
    news_time = models.TextField(max_length=200,null=True)
    def __str__(self):
        return self.news_title

    class Meta:
        ordering = ['-id']