from rest_framework import serializers
from .models import TopNews

class TopNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopNews
        fields = '__all__'
