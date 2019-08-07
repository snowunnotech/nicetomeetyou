from news.models import News
from news.serializers import NewsSerializer
from rest_framework import viewsets
from django.shortcuts import render


# from django.http import HttpResponse
# from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = (IsAuthenticated,)


def news_view(request):
    news = News.objects.all().order_by('-timestamp')
    return render(request, 'hello.html', locals())



