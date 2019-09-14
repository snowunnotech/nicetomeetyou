from django.db import models


class Article(models.Model):
    a_title = models.CharField(max_length=200, unique=True)
    a_datetime = models.DateTimeField()
    a_source = models.CharField(max_length=50)
    a_content = models.TextField()
