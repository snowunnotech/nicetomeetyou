from rest_framework import serializers
from .models import NBASpotNews

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = NBASpotNews
		fields = '__all__'