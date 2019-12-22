from django.shortcuts import render
from rest_framework import viewsets
from nbaNews.models import Post
from nbaNews.serializers import PostSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

