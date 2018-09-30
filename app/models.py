"""
Definition of models.
"""

from django.db import models

# Create your models here.

class News(models.Model):
    Time = models.DateTimeField(null=True)
    Title = models.CharField(max_length=50)
    Url = models.CharField(max_length=100)
    Image = models.CharField(max_length=100)
    Content = models.CharField(max_length=100)
    Detail = models.CharField(max_length=1000,null=True)
    class Meta:
        managed = True
        db_table = 'News'

class SystemLog(models.Model):
    Time = models.DateTimeField()
    Message = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'SystemLog'
