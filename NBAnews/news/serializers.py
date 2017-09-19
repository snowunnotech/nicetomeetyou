from rest_framework import serializers
from news.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('news_id', 'date', 'title', 'content')
