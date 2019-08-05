from rest_framework import serializers
from .models import HotNews


class HotNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotNews
        fields = ("url", "title", "author", "published_datetime", "contents")
