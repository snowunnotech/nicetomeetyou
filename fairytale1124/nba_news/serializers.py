from rest_framework import serializers
from nba_news.models import NewsTable

class NewsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTable
        fields = '__all__'