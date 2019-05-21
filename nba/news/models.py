from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    crawled_time = models.DateTimeField()
    content = models.TextField()
    image_url = models.TextField()
    published_time = models.DateTimeField()

    def __str__(self):
        return "News No." + str(self.id)

    class Meta:
        ordering = ('crawled_time',)
        db_table = "news"










