from django.db import models

# Create your models here.
from django.db import models
# from django.urls import reverse

class Entry(models.Model):
    title = models.CharField(max_length=128, verbose_name='文章標題')
    author = models.CharField(max_length=128, verbose_name='文章作者')
    body = models.TextField(verbose_name='內文')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='創建時間')
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('focus:focusnews_detail', kwargs={'focusnews_id':self.id}) #http://127.0.0.1/focusnews/3
    class Meta:
        ordering = ['-id']
        verbose_name = '焦點文章'
        verbose_name_plural = '焦點文章'