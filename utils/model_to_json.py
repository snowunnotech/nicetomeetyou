# -*- coding: utf-8 -*-

from utils.model_to_dict import get_dict_from_news
import json

def get_json_from_news(news):
    news_dict = get_dict_from_news(news)

    news_json = json.dumps(news_dict)
    return news_json