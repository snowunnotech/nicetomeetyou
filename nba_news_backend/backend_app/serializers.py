"""
The serializer for the model
"""
from rest_framework import serializers
from .models import TaskItem, ArticleItem

class TaskItemSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for TaskItem
    """
    # override dt fields with prefered format
    created_dt = serializers.DateTimeField(
        format="%Y/%m/%d %H:%M:%S",
        required=False)
    ended_dt = serializers.DateTimeField(
        format="%Y/%m/%d %H:%M:%S",
        required=False)
    class Meta:
        model = TaskItem
        fields = '__all__'

class ArticleItemSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for ArticleItem
    """
    # override dt fields with prefered format
    publish_dt = serializers.DateTimeField(
        format="%Y/%m/%d %H:%M:%S",
        required=False)

    class Meta:
        model = ArticleItem
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for ArticleItem (list)
    """
    # override dt fields with prefered format
    publish_dt = serializers.DateTimeField(
        format="%Y/%m/%d %H:%M:%S",
        required=False)

    class Meta:
        model = ArticleItem
        fields = ('id', 'title', 'publish_dt')
