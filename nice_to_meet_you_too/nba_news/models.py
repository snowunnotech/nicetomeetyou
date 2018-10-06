from django.db import models

class NbaNews(models.Model):
    created = models.DateTimeField(blank = True, default = '')
    title = models.CharField(max_length = 100, blank = True, default='')
    author = models.CharField(max_length = 100, blank = True, default = '')
    context = models.CharField(max_length = 1000,  blank = True, default = '')
    photo = models.URLField(blank = True, default = '')
    video = models.URLField(blank = True, default = '')
