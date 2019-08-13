from django.db import models

# Create your models here.

class News(models.Model):

    url_id = models.IntegerField('新聞ID', primary_key=True)
    url_detail = models.URLField('詳細頁面網址', null=True, blank=True)
    image = models.URLField('照片', null=True, blank=True)
    time = models.CharField('更新時間', max_length=50, null=True, blank=True)
    title = models.CharField('標題', max_length=50, null=True, blank=True)
    statement = models.CharField('簡短敘述', max_length=50, null=True, blank=True)
    author = models.CharField('作者', max_length=50, null=True, blank=True)
    author_time = models.DateTimeField('發表時間', null=True, blank=True)
    body_content = models.TextField('詳細內文', null=True, blank=True)
