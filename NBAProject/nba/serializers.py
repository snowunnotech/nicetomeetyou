from rest_framework import serializers
from nba.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
#         fields = ('title', 'content', 'publishedtime', 'web_link')