from rest_framework import serializers
from . models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ('id', 'title', 'author', 'url', 'created_time', 'news_time', 'contents', 'photo')
