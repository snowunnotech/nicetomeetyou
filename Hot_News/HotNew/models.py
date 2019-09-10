from django.db import models

# Create your models here.


class HotNews(models.Model):
    title = models.CharField("新聞標題", max_length=255)
    url = models.URLField("新聞網址", default='')