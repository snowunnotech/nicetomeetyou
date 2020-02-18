from django.db import models
#from django.utils.text import slugify
from uuslug import slugify
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(null = True, blank = True)
    category = models.CharField(max_length=10, null = True, blank = True)
    office = models.CharField(max_length=10, null = True, blank = True)
    author = models.CharField(max_length=10, null = True, blank = True)
    content = models.TextField()
    slug = models.SlugField(null= True, blank = True, max_length = 500)
    url = models.CharField(max_length=100, null = True, blank = True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

