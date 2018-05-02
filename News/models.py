from django.db import models
from datetime import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField(max_length=300)
    img_url = models.URLField(max_length=300)
    content = models.TextField(max_length=500, blank=True)
    time = models.DateTimeField(default=datetime.now)    

    def __str__(self):
        return self.title