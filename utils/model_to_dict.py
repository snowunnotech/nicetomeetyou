# -*- coding: utf-8 -*-
import time

def get_dict_from_news(news):
    # 因為create time時間精確到微秒，而轉換為json會有問題，故先進行去微秒的動作(有bug有時不用轉，有時又要轉)
    created_date_timeStemp = time.localtime(int(time.mktime(news.created_date.timetuple())))
    format_time = time.strftime("%Y-%m-%d %H:%M:%S", created_date_timeStemp)

    # news.created_date
    news_dict = {
        'id': news.id,
        'title': news.title,
        'author': news.author,
        'content': news.content,
        'news_url': news.news_url,
        'org_news_date': news.org_news_date,
        'created_date': format_time
    }

    return news_dict

def get_list_from_newses(newses):
    newses_list = list()
    for news in newses:
        news_dict = get_dict_from_news(news)
        newses_list.append(news_dict)
    return newses_list

def get_dict_from_newses(newses):
    newses_dict = dict()
    i = 0
    for news in newses:
        news_dict = get_dict_from_news(news)
        newses_dict[i] = news_dict
        i += 1
    return newses_dict