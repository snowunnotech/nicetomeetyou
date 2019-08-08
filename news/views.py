from news.models import News, NewsStory
from news.serializers import NewsSerializer
from rest_framework import viewsets
from django.shortcuts import render
from dwebsocket.decorators import accept_websocket, require_websocket

# from django.http import HttpResponse
# from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = (IsAuthenticated,)


class NewsStoryViewSet(viewsets.ModelViewSet):
    queryset = NewsStory.objects.all()
    serializer_class = NewsSerializer


# Http and WebSocket Protocol
@accept_websocket
def news_view(request):
    news = News.objects.all().order_by('-timestamp')
    news_storys = NewsStory.objects.all()
    return render(request, 'hello.html', locals())


@require_websocket
def echo_once(request):
    print('124', request)
    message = request.websocket.wait()
    return request.websocket.send(message)
