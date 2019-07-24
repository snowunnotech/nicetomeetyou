from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    news_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    photo = models.URLField(blank=True)
    contents = models.TextField()

    class Meta:
        db_table = "news"