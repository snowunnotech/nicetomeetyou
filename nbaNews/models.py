from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    img_url = models.CharField(default="no image provide", max_length=250)
    publish_date = models.DateField()

    class Meta:
        db_table = "news"
