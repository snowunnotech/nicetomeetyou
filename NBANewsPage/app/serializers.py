from rest_framework import serializers
from app.models import NBANewsPage

class NBASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NBANewsPage
        fields = ['title', 'href', 'content']