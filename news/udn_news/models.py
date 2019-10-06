from django.db import models
from django.utils import timezone
# Create your models here.


class TopNews(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    title = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    data = models.TextField()

    class Meta:
        app_label = 'udn_news'
        db_table = 'top_news_spider'
        ordering = ['-date']
