from rest_framework import serializers
from nbascrap.models import NbaNews

class NbaNewsSerializer(serializers.ModelSerializer):
    post_datetime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = NbaNews
        fields = ('id', 'title', 'content', 'post_datetime', 'image_url')