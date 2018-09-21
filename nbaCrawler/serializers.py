from rest_framework import serializers
from nbaCrawler.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'pid', 'post_title', 'post_url', 'post_image_url', 'post_date', 'post_content')