from django.db import models
from datetime import datetime
# Create your models here.


class Headline(models.Model):
    headline_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.headline_text


class Article(models.Model):
    headline = models.OneToOneField(Headline, on_delete=models.CASCADE, blank=True)
    article_text = models.TextField()

    def __str__(self):
        return self.article_text
