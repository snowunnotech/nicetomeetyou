
from rest_framework import serializers

from .models import New

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'url', 'title_image_url', 'title', 'content', 'create_datetime')
