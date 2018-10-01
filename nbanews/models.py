from django.db import models

# Create your models here.

class NBANewsModel(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    feature_pic = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title