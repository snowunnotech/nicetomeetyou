from django.db import models

# Add primary key to news_id to avoid same news
class NewsInfo(models.Model):
    news_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length = 100)
    time = models.DateTimeField()
    reporter = models.CharField(max_length = 20)
    link = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)
    content = models.TextField()

    class Meta:
        db_table = "nba"