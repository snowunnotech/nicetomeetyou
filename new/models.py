from django.db import models

# Create your models here.
class new(models.Model):
    id=models.AutoField(primary_key=True)
    article=models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    detail = models.TextField()