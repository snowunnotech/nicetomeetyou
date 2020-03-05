from main_site.models import News
from rest_framework import serializers

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = [
            'news_id',
            'title',
            'author',
            'context', 
            'news_url', 
            'img_url', 
            'post_date', 
            'create_date',
            ]