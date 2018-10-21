from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from news.models import News
from .serializers import NewsSerializers
from .crawl import crawlCornJob

# Create your views here.
class Get_All_News(APIView):
    def get(self, request):
        news = News.objects.all()
        serialized = NewsSerializers(news, many=True)
        return Response(serialized.data)

def render_news(request):
    return render(request, 'news.html')

def redirect_news(request):
     return redirect("/news")

def crawl(request):
    crawlCornJob()
    return HttpResponse('crawling')

def render_stroy(request, uuid):
    story = News.objects.get(uuid=uuid)
    render_dict = model_to_dict(story)
    return render(request, 'story.html', render_dict)

