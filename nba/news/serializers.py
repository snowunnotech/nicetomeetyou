from rest_framework import serializers
from news.models import News
import pytz


class NewsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        timezone = pytz.timezone("Asia/Taipei")
        representation["crawled_time"] = instance.crawled_time.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S")
        representation["published_time"] = instance.published_time.strftime("%Y-%m-%d %H:%M")
        return representation
    class Meta:
        model = News
        fields = ("id", "title", "crawled_time", "published_time")


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "content", "image_url")
