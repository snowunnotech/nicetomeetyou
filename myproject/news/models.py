from django.db import models
import datetime


# Create your models here.
class NBANewsModel(models.Model):
    title = models.CharField(max_length=120)
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('publish_date',)
