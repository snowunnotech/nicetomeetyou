from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    detail = models.TextField()
    url = models.URLField()
    pic_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
