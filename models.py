from django.db import models

# Create your models here.
class hotnew(models.Model):
	new_id = models.CharField(max_length=10) #新聞編號
	new_title = models.CharField(max_length=20) #新聞標題
	new_link = models.URLField(blank=True) #新聞連結
	
	def _str_(self):
		return self.new_title