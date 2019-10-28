from django.db import models


# Create your models here.
class Stock(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, verbose_name='標題')  # Field name made lowercase.
    link = models.URLField(db_column='Link', max_length=500, verbose_name='連結')  # Field name made lowercase.
    context = models.TextField(db_column='Context', verbose_name='內文')  # Field name made lowercase.
    created_time = models.DateTimeField(auto_now=True, verbose_name='爬回時間')

    class Meta:
        managed = True
        db_table = 'stock'

    def __str__(self):
        return self.name





