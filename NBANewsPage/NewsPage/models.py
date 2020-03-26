from django.db import models

# Create your models here.
class NBANewsPage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, verbose_name='標題')
    href = models.CharField(max_length=256, verbose_name='連結')
    content = models.TextField(null = False)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="新增日期")

    def __str__(self):
        return self.title