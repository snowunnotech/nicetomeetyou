from django.db import models

# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=50,null=False)
    content=models.CharField(max_length=255,null=False)
    link_path=models.CharField(max_length=255,null=False)
    src = models.CharField(max_length=150,null=False,default="")
    time=models.DateTimeField(auto_now=True,blank=True)