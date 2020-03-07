from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class NBASpotNews(models.Model):
	news_title = models.TextField(default='')
	report_time = models.DateTimeField()
	report_source = models.TextField(default='')
	report_url = models.TextField(default='')
	photo_url = models.TextField(default='')
	content = models.TextField(default='')
	slug = models.SlugField(null= True, blank = True, max_length = 200)

	def __str__(self):
		return self.news_title

	def get_absolute_url(self):
		return reverse('news_detail', args=[self.slug])

class LatestNewsTitle(models.Model):
	latest_news_title = models.TextField(default='')

	def __str__(self):
		return self.latest_news_title
