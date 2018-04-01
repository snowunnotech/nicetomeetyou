from django.shortcuts import render
from datetime import datetime
# Create your views here.

from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer

def get_articles(request):
    article_list = Article.objects.all()
    return render(request, 'article_list.html', {
        'article_list': article_list,
    })

def article_detail(request, pk):
    print(pk)
    print(type(pk))
    article = Article.objects.get(id=pk)
    return render(request, 'article_detail.html', {
        'article': article,
    })

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer