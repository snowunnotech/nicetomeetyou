from rest_framework import serializers
from news.models import News, NewsStory


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        # news_storys = NewsStory
        fields = '__all__'

