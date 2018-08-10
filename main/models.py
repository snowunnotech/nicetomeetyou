from django.db import models
from django.urls import reverse


class News(models.Model):
    url = models.URLField(max_length=200)
    pub_time = models.DateTimeField(null=True, blank=True)
    crawl_time = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-pub_time', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.id})
