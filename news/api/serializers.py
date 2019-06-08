""" This modules contains serializers for News """
from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    """
    News NewsSerializer for all fields
    """
    class Meta:
        model = News
        fields = ('title', 'url', 'created_at', 'content', 'scrapped_at')
