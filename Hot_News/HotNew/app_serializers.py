from rest_framework import serializers  # DRF 序列化使用

class HotNewsSerializers(serializers.Serializer):              
    title = serializers.CharField(max_length=255)
    url = serializers.URLField(default='')

