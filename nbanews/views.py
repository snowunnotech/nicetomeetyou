from django.shortcuts import render, redirect
from nbanews import models
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.

def index(request):
    # nbanews = models.NBANewsModel.objects.all()
    nbanews = models.NBANewsModel.objects.order_by('-id').values('id', 'title','feature_pic','created_at')
    return render(request, "index.html", locals())

def detail(request, newid=None):
    resp = {}
    try:
        post = models.NBANewsModel.objects.get(id=newid)  # 取得新聞內容
        new = {}
        new['id'] = post.id
        new['feature_pic'] = post.feature_pic
        new['title'] = post.title
        new['content'] = post.content
        new['created_at'] = post.created_at

        resp['status'] = 'success'
        resp['data'] = new
        resp['message'] = '成功撈取訊息'
    except models.NBANewsModel.DoesNotExist:
        resp['status'] = 'error'
        resp['message'] = '找不到資料'
    return JsonResponse(resp)

def checkLatest(request,newscount=None):
    nbanews = models.NBANewsModel.objects.order_by('-id').all()

    resp = {}
    resp['status'] = 'success'
    resp['data'] = []
    resp['message'] = '有新的焦點新聞'

    if nbanews.count() > int(newscount):
        latestnews = nbanews[:nbanews.count()-int(newscount)]
        # return HttpResponse(latestnews[0].content)
        for latestnew in latestnews:
            tmp = {
                'id': latestnew.id,
                'title': latestnew.title,
                'feature_pic': latestnew.feature_pic,
                'content': latestnew.content,
                'created_at': latestnew.created_at,
            }
            resp['data'].append(tmp)
    else:
        resp['status'] = 'error'
        resp['data'] = []
        resp['message'] = '沒有新的焦點新聞'

    return JsonResponse(resp)