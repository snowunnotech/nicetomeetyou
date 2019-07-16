from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField()
    link = models.TextField(unique=True)
    pic_link = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
