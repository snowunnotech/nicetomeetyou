from rest_framework import serializers
from .models import NBANews

class NewsListSerializer(serializers.ModelSerializer):

	class Meta:
		model = NBANews
		fields = ('news_id', 'title', 'date')

class NewsSerializer(serializers.ModelSerializer):

	class Meta:
		model = NBANews
		fields = '__all__'