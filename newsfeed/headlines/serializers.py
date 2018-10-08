from rest_framework import serializers
from newsfeed.headlines.models import HeadlinePost


class HeadlinePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadlinePost
        fields = ('post_id', 'post_title', 'post_date', 
        	'post_content', 'post_url', 'img_url')