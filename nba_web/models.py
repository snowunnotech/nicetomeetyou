from django.db import models


# Create your models here.
class News(models.Model):
    url = models.TextField()
    title = models.TextField()
    update_time = models.DateTimeField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
