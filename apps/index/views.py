from django.shortcuts import render
from django.views.generic.base import View
from .models import Feeds, News
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsSerializer


# Create your views here.

class FeedsView(View):
    def get(self, request):
        all_feeds = Feeds.objects.all()
        return render(request, 'index.html', {'all_feeds': all_feeds})

class Get_News_List(APIView):
    def get(self, request):
        news_list = News.objects.all()
        serialized = NewsSerializer(news_list, many=True)
        return Response(serialized.data)

def Homepage(request): # news list page
    return render(request, 'index.html')
