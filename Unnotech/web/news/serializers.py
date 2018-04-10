from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('article_id', 'author', 'datetime', 'title', 'image_url', 'content', 'url')
