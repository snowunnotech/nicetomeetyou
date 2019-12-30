from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone


class News(models.Model):
	Title = models.CharField(max_length=100, null=False)
	Href = models.CharField(max_length=150,null=False)
	Content = models.TextField()
	Create_at = models.DateField(null=False,default=timezone.now())
	def __str__(self):
		return self.Title
	class Meta:
		db_table = 'News'  # 在資料庫內改名
		ordering = ('-Create_at',)  # 9/24 寫在 models Meta內以降序排列