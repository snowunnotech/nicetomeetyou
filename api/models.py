from django.db import models

class SpotNews(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField()
	author = models.CharField(max_length=30)
	content = models.TextField()
	newsimg = models.TextField(blank=True)

	class Meta:
		db_table = 'SpotNews'

	def __str__(self):
		return self.title