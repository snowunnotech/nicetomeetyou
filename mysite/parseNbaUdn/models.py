from django.db import models
from django.utils import timezone
# Create your models here.


class TopNews(models.Model):
    postId = models.IntegerField()
    title = models.CharField(max_length=60)
    htmlText = models.TextField()
    addingTime = models.DateTimeField('addingTime', default=timezone.now)

    class Meta:
        db_table = 'TopNews'
        ordering = ['-addingTime']

    def __str__(self):
        return self.title
