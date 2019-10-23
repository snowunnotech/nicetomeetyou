from django.db import models


class HotInfo(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField()

    class Meta:
        db_table = 'HotInfo'

    def __str__(self):
        return self.title
