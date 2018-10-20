from rest_framework import serializers

from .models import *

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image_url', 'source_url')
