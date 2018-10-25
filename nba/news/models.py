from django.db import models

# Create your models here.

class newscatch(models.Model):
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    cotent = models.CharField(max_length=1000)
    img = models.CharField(max_length = 500)

    def __str__(self):
        return self.title