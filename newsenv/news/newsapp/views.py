from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from django.shortcuts import render,get_object_or_404

from .models import News
from .serializers import NewsSerializer

def news_detail(request, pk):
   news_list = get_object_or_404(News, pk=pk)
   if news_list is None:
       return HttpResponse(status=404)
   if request.method == 'GET':
       serializer = NewsSerializer(news_list)
       # 将序列化后的数据转换成 json 展示
       return JsonResponse(serializer.data)
   elif request.method == 'PUT':
       data = JSONParser().parser(request)
       serializer = NewsSerializer(news_list, data=data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data)
       return JsonResponse(serializer.errors, status=400)
   # 如果 request 是 DELETE 方法，则直接删除
   elif request.method == 'DELETE':
       news_list.delete()
       return HttpResponse(status=204)

class news_object(APIView):
    def get(self,request,*args,**kwargs):

        news_lists = News.objects.all()

        pg = MyPageNumberPagination()

        page_news_lists = pg.paginate_queryset(queryset=news_lists,request=request,view=self)

        ser = NewsSerializer(instance=page_news_lists,many=True)
        return Response(ser.data)

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 100
    page_query_param = "page"

def news_list(request):

    news_lists = News.objects.all()
    paginator = Paginator(news_lists, 3) 
    page_num = request.GET.get('page', 1) 
    page_of_news = paginator.get_page(page_num) 
    current_page_num = page_of_news.number 
    page_range = list(range(max(1, current_page_num - 2), current_page_num)) + \
                 list(range(current_page_num, min(paginator.num_pages, current_page_num + 2) + 1))

    if page_range[0] -1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] + 2 <= paginator.num_pages:
        page_range.append('...') 
    #加上首頁與尾頁
    if page_range[0] != 1: 
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context={}
    context['news_lists'] = page_of_news.object_list
    context['page_of_news'] = page_of_news
    context['page_range'] = page_range 
    return render(request, 'news_list.html',context)




