from rest_framework import serializers
from nba.models import News

class NbaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'url', 'content', 'time')