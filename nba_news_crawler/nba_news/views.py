from django.shortcuts import render
from nba_news.models import NbaNews
from utils.base_response import Response
from utils.base_response import StatusType
from utils.item import Item


# [GET] /
def index(request):
    return render(request, "index.html")


# [GET] /get_news/
def get_news(request):
    if request.method == "GET":
        items = Item.map(NbaNews.objects.all())
        return Response(items, StatusType.SUCCESS)
    else:
        return Response('', StatusType.WRONG_METHOD)
