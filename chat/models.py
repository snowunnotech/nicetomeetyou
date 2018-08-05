from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    orig_date = models.DateTimeField()
    reporter=models.CharField(max_length=80)


class Paragraph(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    typ  = models.CharField(max_length=10)
    hbody = models.TextField()
 


