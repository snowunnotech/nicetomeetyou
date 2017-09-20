from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    title = models.TextField(default='N/A')
    author = models.TextField(default='N/A')
    issued_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(default='N/A')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"

    def __str__(self):
        return self.title
