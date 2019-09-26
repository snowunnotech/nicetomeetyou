from django.shortcuts import render
from news.models import Articles
from news.serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        articles = Articles.objects.all()
        return Response({'articles': articles})
