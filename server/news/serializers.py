from rest_framework import serializers
from news.models import hotNews


class HotNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hotNews
        # fields = '__all__'
        fields = ['id', 'title', 'href', 'context']