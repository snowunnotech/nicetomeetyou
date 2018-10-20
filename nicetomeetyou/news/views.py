from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import *


def index(request):
    return render(request, "index.html")


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
