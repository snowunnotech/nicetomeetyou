from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'nbanews/index.html', locals())


def detail_view(request, news_id):
    return render(request, 'nbanews/detail.html', locals())