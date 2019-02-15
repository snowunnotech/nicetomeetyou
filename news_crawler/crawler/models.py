from django.db import models

# Create your models here.
class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=25)
    datePublished = models.DateTimeField()
    image = models.URLField()
    context = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "News"
