from django.shortcuts import render
from news.models import News

# Create your views here.
def news_view(request):
    news = News.objects.all().order_by('-id')  # 依據id欄位遞減排序顯示所有資料
    return render(request, 'nba_news.html', locals())


    # return render(request, 'nba_news.html', {
    #     'data': "Hello Django",
    # })