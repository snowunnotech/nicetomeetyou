from rest_framework import serializers

from NBAframework.models import NBAframework


class NBAframeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAframework
        fields = ('id', 'title', 'slug', 'publish_date', 'author', 'image_url', 'image_caption', 'video_url', 'content', 'read')

