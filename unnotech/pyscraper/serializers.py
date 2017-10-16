from rest_framework import serializers
from .models import Headline, Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('article_text',)
        model = Article


class HeadlineSerializer(serializers.ModelSerializer):
    # article = ArticleSerializer(read_only=True)
    article = serializers.SerializerMethodField()

    class Meta:
        # fields = '__all__'
        fields = ('pk', 'headline_text', 'pub_date', 'article')
        model = Headline

    def get_article(self, obj):
        if getattr(obj, 'article', None):
            return obj.article.article_text
