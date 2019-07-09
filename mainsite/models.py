from django.db import models

# Create your models here.


class NewsInfo(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField()

    class Meta:
        db_table = 'NewsInfo'

    def __str__(self):
        return self.title
