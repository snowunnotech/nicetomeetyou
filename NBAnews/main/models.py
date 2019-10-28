from django.db import models


class imgnews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.CharField(max_length=30)
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.title
