from django.db import models

class News(models.Model):
    news_id = models.IntegerField(
        primary_key=True
    )
    author = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=250)
    content = models.TextField()
