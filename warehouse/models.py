from django.db import models

# Create your models here.


class TopNews(models.Model):
    title = models.TextField()
    date = models.TextField()
    data = models.TextField()
