from django.db import models

class NbaNews(models.Model):
    post_id = models.PositiveIntegerField(unique=True)
    reporter = models.CharField(max_length=100, blank=True, default='')
    post_title = models.CharField(max_length=300, blank=True, default='')
    image_url = models.CharField(max_length=1024, blank=True, default='')
    post_url = models.CharField(max_length=1024, blank=True, default='')
    timestamp = models.DateTimeField()
    post_content = models.TextField(blank=True, default='')

    class Meta:
        managed = True
