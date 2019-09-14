from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .serializers import ArticleSerializer
from .models import Article
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



class ArticleList(APIView):
    @method_decorator(cache_page(60*30, cache='default'))
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, 200)


class ArticleDetail(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
    
    @method_decorator(cache_page(60*10, cache='default'))
    def get(self, request, pk, format=None):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
