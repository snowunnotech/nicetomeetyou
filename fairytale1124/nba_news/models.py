from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

class NewsTable(models.Model):
    news_id = models.CharField(max_length=20)
    title = models.TextField()
    url = models.TextField()
    img_url = models.TextField()
    time = models.DateTimeField()
    news_text = models.TextField()

    class Meta:
        db_table = 'news_table'
    def publish(self):
    	self.save()