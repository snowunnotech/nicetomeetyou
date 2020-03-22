from django.db import models

# Create your models here.

class NBANewsPage(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, verbose_name='標題')
    href = models.CharField(max_length=256, verbose_name='連結')
    content = models.TextField()

    class Meta:
        db_table = "News"

    def __str__(self):
        return self.title