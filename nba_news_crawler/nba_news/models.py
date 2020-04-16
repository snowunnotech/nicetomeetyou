from django.db import models


class NbaNews(models.Model):
    url = models.URLField(blank=True)
    image = models.URLField(blank=True)
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self):
        query_result = NbaNews.objects.filter(url=self.url)
        if not query_result:
            super().save()
