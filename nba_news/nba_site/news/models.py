from django.db import models


# Create your models here.
class News(models.Model):
    title = models.TextField()
    url = models.TextField()
    date = models.DateTimeField()
    source = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = "nba_news"