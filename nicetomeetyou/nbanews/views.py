from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from nbanews.models import NbaNews
from nbanews.serializers import NbaNewsSerializers, NbaNewsListSerializers


class GetNbaNewsList(APIView):
    def get(self, request):
        nbanews = NbaNews.objects.all()
        serialized = NbaNewsListSerializers(nbanews, many=True)
        return Response(serialized.data)

class GetNbaNewsDetail(APIView):
    def get(self, request, newsid=None):
        try:
            news = NbaNews.objects.get(post_id=newsid)
        except NbaNews.DoesNotExist:
            return HttpResponse(status=404)
        serialized = NbaNewsSerializers(news)
        return Response(serialized.data)

def news_list(request):
    return render(request, 'news_list.html')
