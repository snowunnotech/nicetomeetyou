from rest_framework import serializers
from focus.models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'url', 'time']
