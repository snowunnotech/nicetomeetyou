from rest_framework import serializers

from .models import News

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'author', 'published_at', 'content']

class NewsIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['uid', 'title']