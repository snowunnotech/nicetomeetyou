from django.db import models


# Create your models here.

class Feeds(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image_url = models.CharField(max_length=100, verbose_name='图片链接')

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='標題',unique = True) # 新聞標題
    image_url = models.CharField(max_length=100, verbose_name='圖片連結') #新聞圖片連結
    short_description = models.CharField(max_length=100, verbose_name='短文字敘述') #簡短文字敘述

    def __str__(self):
    	return self.title


class NewsDetail(models.Model):
    news = models.OneToOneField(
        News,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    detail = models.TextField(max_length = 1000,verbose_name = '內文')    

