from django.db import models

# Create your models here.
class NewsInfo(models.Model):
    title = models.CharField(max_length = 100)
    time = models.CharField(max_length = 50)
    reporter = models.CharField(max_length = 20)
    link = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)
    content = models.TextField()

    def __str__(self):
        return self.title