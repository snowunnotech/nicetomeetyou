from django.db import models

# Create your models here.


class News(models.Model):
    uuid = models.CharField(
        max_length=100, primary_key=True, unique=True, blank=True)
    title = models.CharField(max_length=20)
    published_date = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.uuid
