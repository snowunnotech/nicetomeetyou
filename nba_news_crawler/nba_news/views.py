from django.shortcuts import render
from nba_news.models import NbaNews
from utils.base_response import Response
from utils.base_response import StatusType
from utils.item import Item
import datetime


# [GET] /
def index(request):
    return render(request, "index.html")


# [GET] /get_news/
def get_news(request):
    if request.method == "GET":
        items = get_items(NbaNews.objects.all())
        return Response(items, StatusType.SUCCESS)


def get_items(query_result):
    """
    把 QuerySet 轉成 item

    Args:
        query_result (django.db.models.query.QuerySet): 要解析的 QuerySet
    """
    if not query_result:
        return

    items = []
    for current_query_result in query_result:
        item = Item()
        item['title'] = current_query_result.title
        item['url'] = current_query_result.url
        item['image'] = current_query_result.image
        date = current_query_result.timestamp
        if not date:
            continue
        timestamp = datetime.datetime.timestamp(date)
        item['timestamp'] = timestamp
        items.append(item)
    return items
