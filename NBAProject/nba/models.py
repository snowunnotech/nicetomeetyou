from django.db import models
from django.contrib.auth.models import User #導入內建的使用者模組
# Create your models here.

class News(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishedtime = models.CharField(max_length=20)
    web_link = models.CharField(max_length=100, primary_key=True)
        
    def __str__(self):
        return "<News: %s>" % self.title