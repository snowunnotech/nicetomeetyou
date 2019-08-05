from django.db import models

# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=150, verbose_name="title")
	outline = models.CharField(max_length=300, verbose_name="outline")
	href = models.CharField(max_length=100, verbose_name="href")
	content = models.CharField(max_length=2000, verbose_name="contnet")

	class Meta:
		verbose_name = "dynamic"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title