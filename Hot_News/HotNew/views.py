from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .app_serializers import HotNewsSerializers

from HotNew import models



class get_news(APIView):
    def get(self,request):
        HotNews=models.HotNews.objects.all().order_by('id').reverse()  # 找到所有曾經的熱點新聞，倒序，讓最新的在第一筆
        return render(request,"HotNews.html",{"HotNews":HotNews})


class get_news_title(APIView):
    def post(self,request):    # ajax 找 新聞 URL
        response_state = {"status": True, "error": None, "data": None}         # 返回給前端時的狀態和資料裝在一起

        NewTitle = request.data.get("NewTitle")                                # 取得新聞標題
        show_news_data = models.HotNews.objects.filter(title=NewTitle)         # 找到該新聞的URL
        if show_news_data:                                                     # 判斷該標題是否存在資料庫
            serializers_data = HotNewsSerializers(show_news_data,many=True)    # 開始序列化資料、many 是多筆 或者一筆的意思，  預設是 False 單筆
            response_state["data"] = serializers_data.data[0]["url"]           # 把取得的URL 放進 要返回的狀態字典
            return Response(response_state)
        else:
            response_state["status"] = False
            response_state["error"] = "新聞不存在資料庫，連結失效"
            return Response(response_state)

