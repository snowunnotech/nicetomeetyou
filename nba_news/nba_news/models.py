from django.db import models
# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=256, default='')
    content = models.TextField(default='')
    image_url = models.CharField(max_length=256, default='')
    published_time = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
