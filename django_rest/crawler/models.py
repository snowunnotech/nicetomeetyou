from django.db import models
from uuslug import slugify
from django.urls import reverse
# Create your models here.

class nba_news(models.Model):
    nba_title = models.CharField(max_length = 30, blank=True, default='')
    nba_content = models.TextField(blank=True, default='')
    nba_url = models.TextField(blank=True, default='')
    nba_time = models.CharField(max_length=50, null=True, default='')
    slug = models.SlugField(null= True, blank = True, max_length = 500)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nba_title)
        super(nba_news, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_news', args=[self.slug])
