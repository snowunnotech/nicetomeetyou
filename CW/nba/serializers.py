#coding=utf-8

from rest_framework import serializers

from .models import News

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields =('title','link','content')