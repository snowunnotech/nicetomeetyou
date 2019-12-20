from rest_framework import serializers
from myapp.models import news

class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields='__all__'