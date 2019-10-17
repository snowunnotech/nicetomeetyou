from django.db import models
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class NBAframework(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=100, unique=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    author = models.CharField(max_length=120)
    image_url = models.CharField(max_length=1024, blank=True, null=True)
    image_caption = models.CharField(max_length=120)
    video_url = models.CharField(max_length=1024, blank=True, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('publish_date',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.publish_date)
        super(NBAframework, self).save(*args, **kwargs)