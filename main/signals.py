from django.db.models.signals import post_save
from django.dispatch import receiver
# a common communication channel for all instance
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import News


@receiver(post_save, sender=News)
def news_save_handler(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()

        # group_send is for broadcast
        async_to_sync(channel_layer.group_send)(
            # name of the group
            "news", {
                "type": "news.update",  # name of the group
                "event": "New Post"
            }
        )
