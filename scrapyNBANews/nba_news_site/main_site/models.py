from django.db import models

class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    context = models.TextField()
    news_url = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    post_date = models.DateTimeField()
    create_date = models.DateTimeField()

    class Meta:
        db_table = 'news'