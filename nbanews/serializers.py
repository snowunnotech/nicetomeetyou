from rest_framework import serializers
from nbanews.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('pid', 'title', 'time', 'author', 'img', 'context')
