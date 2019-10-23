from rest_framework import serializers
from .models import HotInfo


class HotInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotInfo
        fields = '__all__'