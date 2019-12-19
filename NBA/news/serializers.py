from rest_framework import serializers
from .models import NBANews


class NBANewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NBANews
        fields = ('id', 'title', 'published', 'text', 'img_url')
