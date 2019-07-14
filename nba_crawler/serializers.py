'''
from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	def __str__(self):
		return self.title
'''
#change to models.py
#refer to https://www.youtube.com/watch?v=S5M1SnLKagg
