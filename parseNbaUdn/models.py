from django.db import models
from django.utils import timezone
# Create your models here.


class TopNews(models.Model):
    postId = models.IntegerField()
    title = models.TextField()
    imgUrl = models.TextField()
    pageUrl = models.TextField()
    addingTime = models.DateTimeField('addingTime', default=timezone.now)

    class Meta:
        db_table = 'TopNews'
        ordering = ['-id']

    def __str__(self):
        return self.title
