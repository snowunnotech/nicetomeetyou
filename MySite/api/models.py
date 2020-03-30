from django.db import models

# Create your models here.
class News(models.Model):
    ID = models.AutoField(primary_key=True) #PK
    CrawlerAt = models.DateTimeField(auto_now=True) #新聞爬取時間
    Title = models.CharField(max_length = 100) #新聞標題
    CreateAt = models.DateTimeField() #新聞發布時間
    Content = models.CharField(max_length = 1000) #新聞內容
    Url = models.CharField(max_length = 1000) #原始連結