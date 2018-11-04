# -*- coding: utf-8 -*-

from news.models import News
import json

def get_news_from_json(news_json):
    news_dict = json.loads(news_json)

    news = News(title=news_dict['title'],
                author=news_dict['author'],
                content=news_dict['content'],
                news_url=news_dict['news_url'])

    if 'org_news_date' in news_dict.keys():
        news.org_news_date = news_dict['org_news_date']
    if 'created_date' in news_dict.keys():
        news.created_date = news_dict['created_date']

    return news
