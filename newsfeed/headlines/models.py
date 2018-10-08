from django.db import models

# Create your models here.
class HeadlinePost(models.Model):
	post_id = models.IntegerField() 
	post_title = models.TextField()
	post_date = models.DateTimeField()
	post_content = models.TextField()
	post_url = models.URLField()
	img_url = models.URLField()

	class Meta:
		db_table = "headlinepost"