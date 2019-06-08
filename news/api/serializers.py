""" This modules contains serializers for News """
from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    """
    News NewsSerializer for all fields
    """
    class Meta:
        model = News
        fields = ('id', 'title', 'created_at')

class NewsDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    News NewsSerializer for all fields
    """
    class Meta:
        model = News
        fields = ('id', 'title', 'created_at', 'content')
