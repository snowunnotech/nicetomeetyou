from rest_framework import serializers
from .models import NBANewsPage

class NBASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NBANewsPage()
        fields = ['id', 'title', 'href', 'content', 'add_date']