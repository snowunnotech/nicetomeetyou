from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from nba_news.nba_news.models import Article
from nba_news.nba_news.serializers import ArticleSerializer
from .nba_news_crawler import get_latest_news

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

@api_view(['GET'])
def nba_news(request, article_id):
    news = Article.objects.filter(article_id=article_id)[0]
    rtn_news = ArticleSerializer(news).data
    return Response(rtn_news, status=status.HTTP_200_OK)

@api_view(['GET'])
def all_nba_news(request):
    rtn_news_list = list()
    news_list = Article.objects.all()

    for news in news_list:
        rtn_news_list.append(ArticleSerializer(news).data)

    return Response(rtn_news_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def nba_news_list(request):
    rtn_news_list = list()
    news_list = Article.objects.all()[::-1]

    for news in news_list:
        rtn_news_list.append(ArticleSerializer(news).data)

    return render(request, "index.html", {'news_list': rtn_news_list})

@api_view(['GET'])
def update_news_data(request):
    existed_articles = Article.objects.all()
    crawled_news = get_latest_news()

    for news in crawled_news:
        if existed_articles.filter(title=news['title']):
            continue
        new_news = Article(title=news['title'],
                           url=news['url'],
                           content=news['content'],
                           image_url=news['image_url'],
                           published_time=news['published_time'])
        new_news.save()

    return Response("Success", status=status.HTTP_200_OK)
