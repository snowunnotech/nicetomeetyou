import datetime
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField(default='N/A')
    author = models.TextField(default='N/A')
    issued_date = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField(default='N/A')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
