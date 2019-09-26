from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()
    pub_time = models.DateTimeField()

    class Meta:
        ordering = ['-pub_time']
