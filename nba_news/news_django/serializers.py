from rest_framework import serializers
from .models import News_model

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_model
        fields = ("news_id", "title", "published_time")
    
class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_model
        fields = ("title", "content", "figure_url", "published_time")
        