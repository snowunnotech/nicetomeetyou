from django.db import models

# Create your models here.

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    imgsrc = models.TextField(blank=True, null=True)
    detailsrc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'