from django.db import models

class News(models.Model):
    pid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    time = models.DateTimeField()
    author = models.CharField(max_length=20)
    img = models.URLField()
    context = models.TextField()

    class Meta:
        db_table = "nba_news"
