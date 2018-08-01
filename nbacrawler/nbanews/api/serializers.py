from rest_framework import serializers

from ..models import NBANewsModel


class NBANewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBANewsModel
        fields = ('id', 'title', 'slug', 'publish_date', 'author', 'image_url', 'image_caption', 'video_url', 'content', 'read')

