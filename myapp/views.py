from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

def homepage(request):
    try:
        latest_time = Latest.objects.all()[0].latest_news.post_time.replace(tzinfo=None)
        update_news(latest_time)
        return render(request, "homepage.html", {"all_news":News.objects.all()})
    except Exception as e:
        print(e)


def content(request):
    print("content")
    _id = request.GET['id']
    content = News.objects.filter(id=_id)[0].content
    print(content)
    return JsonResponse({"content":content})
