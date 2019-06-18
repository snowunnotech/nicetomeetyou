from rest_framework import serializers
from nba_web.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # fields = ('id', 'url', 'update_time', 'content', 'created')
