from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class NBANews(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=250)
    #slug = models.SlgField(unique=True, max_length=250)
    published = models.DateTimeField()
    text= models.TextField()
    img_url = models.TextField()

    class Meta:
        ordering = ('published',)