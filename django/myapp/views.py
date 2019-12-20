from django.shortcuts import render
from bs4 import BeautifulSoup
import requests,re
#import time
from myapp.models import news
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

#Ajx news
def get_news_api(request):
    unit=news.objects.all()
    data=serializers.serialize('json',unit)
    return JsonResponse({'data':data})

# news table 
def index(request):
    return render(request,'news.html',locals())
# news detail
def detail(request,id):
    unit=news.objects.get(id=id)
    # time=unit.time
    # title=unit.title
    # content=unit.content
    return render(request,'detail.html',locals())

# # detail 
# def get_news(request,news_id):
#     unit=news.objects.get(pk=news_id)
#     time=unit.time

#     return render(request,'detail.html',locals())


def newsapi(request):
    url=requests.get("https://nba.udn.com/nba/index?gr=www")
    #if url.status_code==requests.codes.ok:
    #     print('連線成功！！')
    # else:
    #     print('連線失敗')
    #xtime=time.localtime()
    #newtime=time.asctime(xtime)
    res=BeautifulSoup(url.text,'html.parser')
    src=[]
    for img in res.find_all("img",{"src":re.compile('\.jpg')}):
      #print(img["src"])
      #print("_"*40)
      src.append(img["src"])
    
    
    res=res.find("div","box")
    
    link=[]
    
    res1=res
    links = res1.find_all("a",{"href": re.compile('nba')})
    for link1 in links[1:4]:
      link.append("https://nba.udn.com/"+link1['href'])
    
    
    
    
    
    #content
    res2=res.find_all("dt")
    title=[]
    content=[]
    for i in res2[:3]:
        title.append(i.h3.text)
        content.append(i.p.text.strip())
       
        
        
    
    all = zip(title,content,link,src)
    #number=2
    
    for title,content,link,src in all:
        try:
            check=news.objects.get(title=title)
        except:
            check=None
        if check != None:
            msg="目前文章已經是最新"
        else:

            unit = news.objects.create(title=title,content=content,link_path=link,src=src)  
            msg="有新文章更新囉！！"
            unit.save()
    
    return render(request,'index.html',locals())
