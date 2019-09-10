from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class NBANews(models.Model):

	news_id = models.CharField("id", default="0000_0000000", max_length=15, unique=True)
	title = models.CharField("Title", max_length=255)
	date = models.DateTimeField("Date", default = timezone.now)
	author = models.CharField("Author", max_length=255)
	content = models.TextField("content", max_length=4096)
	
	class Meta:
		app_label = 'UdnNBANewsParser'
		db_table = 'nba_news'
		
	def __str__(self):
		return self.title