from django.db import models

# Create your models here.

class TopNews(models.Model):
    link = models.CharField(max_length=300, unique=True)
    photo = models.CharField(max_length=300)
    headline = models.CharField(max_length=300)
    body = models.CharField(max_length=300)

    class Meta:
        app_label = 'warehouse'
        db_table = 'top_news'
