from news.models import News, NewsStory
from news.serializers import NewsSerializer
from rest_framework import viewsets
from django.shortcuts import render

# from django.http import HttpResponse
# from rest_framework.permissions import IsAuthenticated

# dwebsocket has something wrong when websocket connect
# from dwebsocket.decorators import accept_websocket, require_websocket


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = (IsAuthenticated,)


class NewsStoryViewSet(viewsets.ModelViewSet):
    queryset = NewsStory.objects.all()
    serializer_class = NewsSerializer


def news_view(request):
    news = News.objects.all().order_by('-timestamp')
    news_storys = NewsStory.objects.all().order_by('-parent_id')
    return render(request, 'hello.html', locals())


# def echo_once(request):
#     print('124', request)
#     message = request.websocket.wait()
#     return request.websocket.send(message)
