from news.models import News
from rest_framework import serializers


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'published_date', 'text')
