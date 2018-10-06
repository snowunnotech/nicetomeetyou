from nba_news.models import NbaNews
from rest_framework import serializers

class NbaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NbaNews
        fields = ('id', 
                  'created',
                  'title',
                  'author',
                  'context',
                  'photo',
                  'video')
