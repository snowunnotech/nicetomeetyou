from django.shortcuts import render
import requests

from .models import TopNews
from .parser import TopNewsParser

# Create your views here.


def task(request):
    url = 'https://nba.udn.com/nba/index?gr=www'
    page = requests.get(url)
    p = TopNewsParser(url)
    p.feed(page.text)
    for n in p.newsList:
        try:
            TopNews.objects.get(postId=n.postId)
        except TopNews.DoesNotExist:
            TopNews(postId=n.postId, title=n.title, imgUrl=n.imgUrl, pageUrl=n.pageUrl).save()
        finally:
            pass

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer