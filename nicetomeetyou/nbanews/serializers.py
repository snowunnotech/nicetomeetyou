from rest_framework import serializers
from nbanews.models import NbaNews



class NbaNewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = NbaNews
        fields = ('post_title', 'post_id')

class NbaNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NbaNews
        fields = '__all__'

