from django.shortcuts import render
from main.models import News
from rest_framework import viewsets
from main.serializers import NewsSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
import os


class NewsViewSet(viewsets.ModelViewSet):
    # 依照新聞 PO 出時間倒序
    queryset = News.objects.all().order_by('-post_date')
    serializer_class = NewsSerializer

    # 刪除最近一筆新聞的 API，以便測試
    @action(methods=['post'], detail=False, url_path='delete-the-latest-news')
    def delete_the_latest_news(self, request):

        # 若還有新聞
        if News.objects.all().count() > 0:

            News.objects.all().order_by('-post_date')[0].delete()

            return JsonResponse({'status': True}, status=200)
        
        else:
            
            return JsonResponse({'status': False}, status=200)


def Index(request):
    os_name = os.name #用來判斷目前是 Local 還是 Production
    return render(request, 'main/index.html', locals())

def NewsDetail(request, news_id):
    news_id = news_id
    return render(request, 'main/news-detail.html', locals())