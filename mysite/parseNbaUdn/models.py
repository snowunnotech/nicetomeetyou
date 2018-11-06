from django.db import models

# Create your models here.

class topNews(models.Model):
    postId = models.TextField()
    title = models.TextField()
    text = models.TextField()
    img = models.TextField()
    pageUrl = models.TextField()

    class Meta:
        db_table = 'topNews'