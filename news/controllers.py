# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from news.models import News
from utils.json_to_model import get_news_from_json
from utils.model_to_dict import get_list_from_newses, get_dict_from_newses, get_dict_from_news
from errors.general import get_other_error, error_handler
from errors.model import get_not_news_found_error, get_found_duplicated_news_error

from django.db.utils import IntegrityError

# 導入新聞至數據庫
def import_news(request):
    return_dict = None
    try:
        news_json = request.POST.get('news_json')
        news = get_news_from_json(news_json)
        news.save()
        return_dict = {
            'msg': '成功'
        }
    except IntegrityError as e:
        return_dict = get_found_duplicated_news_error()
        error_handler(e)
    except Exception as e:
        return_dict = get_other_error()
        error_handler(e)
    finally:
        return JsonResponse(return_dict, safe=False)

def get_news_for_table_data(request):
    return_dict = None
    try:
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        end = start + length

        newses = News.objects.all()[start:end]
        return_dict = {
            "draw": draw,
            "recordsTotal": getNewsCount(),
            "recordsFiltered": getNewsCount(),
            "data": get_list_from_newses(newses)
        }
    except Exception as e:
        return_dict = get_other_error()
        error_handler(e)
    finally:
        return JsonResponse(return_dict, safe=False)

# 通過前置量與後置量，取得新聞列表
def get_newses_dict(request, offset, limit, desc):
    return_dict = None
    try:
        offset = int(offset)
        limit = int(limit)
        desc = int(desc)

        # 排序方式，依照新聞發布日期
        sort_rule = 'org_news_date'
        if desc > 0:
            sort_rule = '-' + sort_rule

        newses = News.objects.all().order_by(sort_rule)[offset:limit]
        return_dict = get_dict_from_newses(newses)
    except Exception as e:
        return_dict = get_other_error()
        error_handler(e)
    return JsonResponse(return_dict)

def getNewsCount():
    count = News.objects.all().count()
    return count
# 取得新聞總條數
def get_newes_count(request):
    return_dict = None
    try:
        count = getNewsCount()
        return_dict = {
            'count': count
        }
    # 其他問題
    except Exception as e:
        return_dict = get_other_error()
        error_handler(e)
    finally:
        return JsonResponse(return_dict, safe=False)

# 通過id取得新聞
def get_news_by_id(request, id):
    return_dict = None

    try:
        news = News.objects.get(id=id)
        return_dict = get_dict_from_news(news)

    # 找不到新聞的例外處理
    except News.DoesNotExist as e:
        return_dict = get_not_news_found_error(id)

    # 其他問題
    except Exception as e:
        return_dict = get_other_error()
        error_handler(e)
    finally:
        return JsonResponse(return_dict, safe=False)