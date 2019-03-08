from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    uploadDatetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = News
        ordering = ('seqNum',)
        fields = ('id', 'title', 'url', 'content',
                  'uploadDatetime',)
