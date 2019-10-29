from rest_framework import serializers
from .models import NewsModel

class NewsSerializer(serializers.ModelSerializer):
    """translate model info into Json """

    class Meta:
        """specifying attributes"""
        model = NewsModel
        fields = ('id', 'title', 'link_url', 'img_url')