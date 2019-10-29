from rest_framework import serializers
from .models import SpotNews

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SpotNews
		fields = ('id', 'title', 'date', 'author', 'content')