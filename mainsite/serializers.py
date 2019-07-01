from rest_framework import serializers
from .models import news_record

class news_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = news_record
        fields = '__all__'