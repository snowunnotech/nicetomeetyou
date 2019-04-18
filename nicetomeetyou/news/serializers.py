from rest_framework import serializers
from . models import News


class NewsSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=200)
    contents = serializers.CharField()
    published_date = serializers.DateTimeField()
    created_date = serializers.DateTimeField(read_only=True)
