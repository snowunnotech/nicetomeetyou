from django.db import models
from django.urls import reverse


def upload_image_path():
    pass


class NewsManager(models.Manager):
    def is_new(self, url=None):
        qs = self.get_queryset().filter(url=url)
        if qs.exists():
            return False
        return True


class News(models.Model):
    url = models.URLField(max_length=200)
    pub_time = models.DateTimeField(null=True, blank=True)
    crawl_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    objects = NewsManager()

    class Meta:
        ordering = ['-pub_time', ]

    def __str__(self):
        if self.title:
            return self.title
        return str(self.id)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.id})


class Photo(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    alt = models.TextField(blank=True, null=True)
    src = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(str(self.news), str(self.id))
