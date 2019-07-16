from django.shortcuts import render
from .models import NBANewsModel


# Create your views here.
def news_list(request):
    news = NBANewsModel.objects.all().order_by('-publish_date')
    return render(request, 'news/news_list.html', {'news': news})


def news_content(request, id):
    news = NBANewsModel.objects.get(id=id)
    return render(request, 'news/news_content.html', locals())
