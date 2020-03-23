from django.db import models


class NbaSpider(models.Model):
    created_at = models.DateTimeField(null=False),
    publish_at = models.CharField(null=False),
    author = models.CharField(null=False, max_length=100),
    title = models.CharField(null=False, max_length=30),
    content = models.TextField(null=False),
    news_url = models.TextField(null=False)

    def __str__(self):
        return self.title

