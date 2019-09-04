from django.db import models

# Create your models here.

class NewsPost(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True)
    para1 = models.TextField(blank=True)
    para2 = models.TextField(blank=True)
    para3 = models.TextField(blank=True)
    para4 = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "newspost"
