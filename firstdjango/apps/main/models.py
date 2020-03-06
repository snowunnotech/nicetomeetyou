from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    link_url = models.CharField(max_length=100, verbose_name='link')

    class Meta:
        verbose_name = 'XXX'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

