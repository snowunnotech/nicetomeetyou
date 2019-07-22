from .models import NBA
from rest_framework import serializers

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NBA
        fields = ['id', 'title', 'date_time', 'author', 'content', 'image_source', 'video_source', 'article_url']