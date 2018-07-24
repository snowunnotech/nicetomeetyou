from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer

class Index(APIView):
    
    def get(self, request):
        return render(request, 'index.html')

class NewsList(APIView):

    def get(self, request):
        news_list = News.objects \
            .all() \
            .values("id", "title", "datetime") \
            .order_by('-id')
        return Response(news_list)

class NewsDetail(APIView):

    def get(self, request, id):
        news_detail = News.objects.filter(id=id)
        return Response(model_to_dict(news_detail[0]))
