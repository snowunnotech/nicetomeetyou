from channels import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from news.models import News


@receiver(post_save, sender=News)
def news_updated_post_save(sender, **kwargs):
    #print('Saved: {}'.format(kwargs['instance'].__dict__))
    Group("users").send({'text': 'News Updated!'})