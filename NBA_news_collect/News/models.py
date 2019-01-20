from django.db import models
from django.urls import reverse

# Create your models here.


class News(models.Model):
	#新聞主頁資訊
	title = models.CharField(max_length=250)
	image_url = models.CharField(max_length=250)
	detail_url = models.CharField(max_length=250)
	#新聞內文資訊
	post_date = models.CharField(max_length=250)
	author = models.CharField(max_length=250)
	detail = models.CharField(max_length=1000)
	video_url = models.CharField(max_length=250)







	def get_absolute_url(self):
		return reverse('News:news_detail',
        	            args=[self.id,
                       		  self.post_date,
                          ])

	class Meta:
		ordering = ('-post_date',)

	def __str__(self):
		return self.title
