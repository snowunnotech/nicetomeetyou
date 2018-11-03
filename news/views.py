# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

# 取得新聞列表，用以顯示新聞標題
def news_list(request):
    return render(request, 'news_list.html')

# 取得所有特定ID的新聞
def get_news_view(request, id):
    r = requests.get('http://127.0.0.1:8000/get_news_by_id/id=' + id)
    print(r)
    r_json = r.json()

    # 找不到新聞的處理方式
    if 'error_msg' in r_json.keys():
        return render(request, 'no_news.html')

    title = r_json['title']
    author = r_json['author']
    content = r_json['content']
    org_news_date = r_json['org_news_date']
    created_date = r_json['created_date']

    return render(request, 'get_news.html',
    {
        'title': title,
        'author': author,
        'content': content,
        'org_news_date': org_news_date,
        'created_date': created_date
    })

#https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/django/models.html
#http://www.icodelogic.com/?p=501
#http://dokelung-blog.logdown.com/posts/220833-django-notes-7-forms

# 定時任務
#https://www.jianshu.com/p/f6e80e6125cc