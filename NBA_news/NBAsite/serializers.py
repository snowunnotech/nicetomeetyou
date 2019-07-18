from rest_framework import serializers
from NBAsite.models import NewsInfo


class NbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsInfo
        fields = '__all__'