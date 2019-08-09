
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from nbascrap.models import NbaNews

def home(request):
    context = {}

    news_list = NbaNews.objects.all()

    context['news_list'] = news_list


    return render(request, 'home.html', context)

def news_detail(request, pk):
    context = {}

    news = get_object_or_404(NbaNews, pk=pk)
    context['news'] = news

    return render(request, 'news_detail.html', context)