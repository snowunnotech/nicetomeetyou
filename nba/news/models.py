from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField()
    link = models.TextField(primary_key=True)

    class Meta:
        db_table = "news"
