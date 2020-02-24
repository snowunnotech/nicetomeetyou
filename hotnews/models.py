from django.db import models

class nbahotnews(models.Model):
    ntitle = models.CharField(max_length=200)
    nshortcnt = models.CharField(max_length=1000, blank=True)
    ncontent = models.CharField(max_length=9999, blank=True)
    nlink = models.CharField(max_length=200)
    nimglink = models.CharField(max_length=200, blank=True)
    npubtime = models.DateTimeField('publish_time')
    nauth = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.ntitle
# Create your models here.
