from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import HotNews


class HotNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotNews
        fields = '__all__'
