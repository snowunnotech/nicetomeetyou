from rest_framework import serializers

from news.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("author", "datetime", "title", "image_url", "story_url", "content", "video_url")
