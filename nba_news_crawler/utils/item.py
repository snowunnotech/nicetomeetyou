import datetime
from django.db.models.query import QuerySet


class Item(dict):
    def __init__(self):
        self['title'] = None
        self['url'] = None
        self['image'] = None
        self['timestamp'] = None

    @staticmethod
    def map(query_result: QuerySet):
        """
        把 QuerySet 轉成 item

        Args:
            query_result (django.db.models.query.QuerySet): 要解析的 QuerySet
        """
        if not query_result:
            return None

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
