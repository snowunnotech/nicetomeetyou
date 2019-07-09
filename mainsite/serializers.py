from rest_framework import serializers
from .models import NewsInfo


class NewsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsInfo
        fields = '__all__'
