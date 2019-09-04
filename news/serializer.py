from rest_framework import serializers
from news.models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    
    class Meta:
        model = NewsPost
        fields = ('id', 'title', 'photo_url', 'para1', 'para2', 'para3', 'para4')
