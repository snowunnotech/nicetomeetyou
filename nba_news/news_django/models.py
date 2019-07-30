from django.db import models

# Create your models here.
class News_model(models.Model):
    news_id = models.AutoField(db_column = 'news_id', primary_key = True)
    title = models.TextField(db_column = 'title', max_length=100, default='some title')
    url = models.TextField(db_column = 'url', max_length=100, default='some url')
    content = models.TextField(db_column = 'content', max_length=5000, default='some content')
    figure_url = models.TextField(db_column = 'figure_url', max_length=100, default='some url')
    crawled_time = models.TextField(db_column = 'crawled_time', max_length=50, default='some time')
    published_time = models.TextField(db_column = 'published_time', max_length=50, default='some time')
    
    class Meta:
        db_table = 'news'
