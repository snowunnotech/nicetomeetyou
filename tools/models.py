from django.db import models
from webdata import settings

class cr_nba(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.TextField()
	datetime = models.DateTimeField()
	author = models.TextField(blank=True)
	content = models.TextField()
	url = models.TextField()