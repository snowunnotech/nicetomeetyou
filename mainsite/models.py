from django.db import models

# Create your models here.
class news_record(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()

    def __str__(self):
        return self.title