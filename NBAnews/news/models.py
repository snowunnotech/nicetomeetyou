from django.db import models
from django.utils import timezone
# Create your models here.

class News(models.Model):
    news_id = models.IntegerField()
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
