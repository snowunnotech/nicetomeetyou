from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField()
    link = models.TextField()

    class Meta:
        db_table = "news"
