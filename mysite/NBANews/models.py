from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 100)
    url = models.URLField(primary_key = True)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return  self.title

