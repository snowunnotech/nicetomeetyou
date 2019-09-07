from django.shortcuts import render_to_response, render
# from django.shortcuts import render
from news.models import News

# Create your views here.
def news_view(request):
    news = News.objects.all().order_by('-id')  # 依據id欄位遞減排序顯示所有資料
    return render(request, 'nba_news.html', locals())

def content_view(request):
    content = News.objects.get(id=request.GET['id'])
    return render_to_response('content.html', locals())