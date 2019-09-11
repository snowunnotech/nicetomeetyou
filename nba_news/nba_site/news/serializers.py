from django.utils.timezone import now
from rest_framework import serializers
from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ('id', 'title')


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ('id', 'title', 'url', 'date', 'source', 'content')