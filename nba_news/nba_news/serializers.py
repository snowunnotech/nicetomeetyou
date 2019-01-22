from rest_framework import serializers
from nba_news.nba_news.models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('article_id', 'title', 'content',
                  'image_url', 'published_time')
