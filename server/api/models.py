from django.db import models

# Create your models here.

# python manage.py makemigrations api
# python manage.py migrate

class HotNews(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.TextField()
    news_url = models.CharField(max_length=255, default='')
    image_url = models.CharField(max_length=255, default='')
    post_date = models.DateTimeField(null=True, default=None)