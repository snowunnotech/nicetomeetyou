from django.db import models

# Create your models here.
class NewsModel(models.Model):
    title = models.TextField()
    link_url = models.URLField()
    img_url = models.URLField()

    class Meta:
        unique_together = ['title', 'link_url']

    def __str__(self):
        return self.title