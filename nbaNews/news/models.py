from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    uploadDatetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.url
