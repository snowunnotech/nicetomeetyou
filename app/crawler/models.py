from django.db import models
from django.utils import timezone

# Create your models here.

class NBANewsInFocus(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(NBANewsInFocus, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'nba_news_in_focus'