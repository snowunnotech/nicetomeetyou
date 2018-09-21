from django.db import models

# Create your models here.
class Post(models.Model):
    pid = models.IntegerField()
    post_title = models.CharField(max_length=30)
    post_date = models.DateTimeField()
    post_url = models.TextField()
    post_image_url = models.TextField()
    post_content = models.TextField()

    def __str__(self):
        return self.post_title