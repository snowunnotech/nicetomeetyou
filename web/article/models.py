from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=50)
    date = models.DateField('date')
    content = models.TextField('Content')

    def __unicode__(self):
        return self.title