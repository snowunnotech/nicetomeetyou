from django.db import models

# Create your models here.
class NBAHotNews(models.Model):
	NewsId = models.IntegerField(primary_key=True)
	NewsTitle = models.CharField(max_length=100)
	ImgFileName = models.CharField(max_length=255)
	NewsUpdateDateTime = models.DateTimeField()
	Author = models.CharField(max_length=100)
	NewsDetailContent = models.TextField()
	
	def __str__(self):
		return str(self.NewsId)


from django.db.models.signals import post_save
from django.dispatch import receiver
import channels.layers
from asgiref.sync import async_to_sync


@receiver(post_save, sender=NBAHotNews)
def TestHandler(sender, **kwargs):
	NewsId = kwargs.get('instance').NewsId
	NewsTitle = kwargs.get('instance').NewsTitle
	
	message = {"type":"NewsUpdateNotification", "NewsId":NewsId, "NewsTitle":NewsTitle}
	
	ChannelLayer = channels.layers.get_channel_layer()
	async_to_sync(ChannelLayer.group_send)("NewsUpdateGroup", message)


