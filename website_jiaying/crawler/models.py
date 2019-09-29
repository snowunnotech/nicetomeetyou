from django.db import models
from django.core.validators import URLValidator


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    intro = models.CharField(max_length=200)
    content = models.TextField(default='No Content')
    link = models.TextField(validators=[URLValidator()], default='https://nba.udn.com')
    photo = models.TextField(validators=[URLValidator()], default='https://nba.udn.com')
