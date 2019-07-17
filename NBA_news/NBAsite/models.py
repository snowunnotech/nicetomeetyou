from django.db import models

# Create your models here.
class NewsInfo(models.Model):
    title = models.CharField(max_length = 100)
    time = models.CharField(max_length = 50)
    content = models.TextField()
    image_url = models.CharField(max_length = 100)

    def __str__(self):
        return self.title