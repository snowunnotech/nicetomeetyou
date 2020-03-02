from django.db import models

# Create your models here.


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=3000)

    def __str__(self):
    	return self.title
