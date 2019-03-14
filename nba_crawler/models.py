from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=20)
    top = models.CharField(max_length=50)
    content = models.TextField()
    url = models.URLField(unique=True)
    photo_url = models.URLField()

    class Meta:
        db_table = "news"
