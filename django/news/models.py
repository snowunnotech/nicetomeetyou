from django.db import models


class News(models.Model):
    story_id = models.FloatField(null=False, unique=True)
    headline = models.CharField(null=False, max_length=30)
    image = models.TextField(null=False)
    keywords = models.CharField(null=False, max_length=50)
    author = models.CharField(null=False, max_length=20)
    publisher = models.CharField(null=False, max_length=30)
    logo = models.TextField(null=False)
    figcaption = models.CharField(null=False, max_length=30)
    context = models.TextField(null=False)
    datePublished = models.DateTimeField()
    dateModified = models.DateTimeField()

    def __str__(self):
        return self.headline
