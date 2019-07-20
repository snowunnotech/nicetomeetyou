from django.db import models
from rest_framework import serializers
# Create your models here.

class Catch(models.Model):
    news_id = models.AutoField(db_column='news_id', primary_key=True,)
    title = models.TextField(db_column='title',)
    text = models.TextField(db_column='text',)
    picture = models.TextField(db_column='picture',)
    potime = models.DateTimeField(db_column='potime')

    class Meta:
        db_table = "Catch"
