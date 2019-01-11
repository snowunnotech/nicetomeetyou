from django.db import models

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length=30)
	text = models.CharField(max_length=100)
	detail = models.CharField(max_length=100)
	time = models.CharField(max_length=30)
	img = models.CharField(max_length=100)

	def __str__(self):
		return self.title
