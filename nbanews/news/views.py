from django.shortcuts import render, redirect
from nbanews.loggers import logger

from django.forms.models import model_to_dict
import requests
from bs4 import BeautifulSoup
from news.models import News

def get_newsContent():
    
    '''
        get_newsContent : 取得焦點新聞資料
    '''
    
    newsContent = []
    #抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
    try :
                            
        response = requests.get( 'https://nba.udn.com/nba/index?gr=www', timeout = 5 )
        
        soup = BeautifulSoup( response.text, 'html.parser')
        #找焦點新聞區塊
        newsBody = soup.find(id='news_body')
        #找a
        newsDetail = newsBody.find_all('a')
        
        for news in newsDetail :
            
            newsObj = {}
            
            newsObj['imgsrc'] = news.find('img')['src']
            
            newsObj['title'] = news.find('h3').text
            
            newsObj['content'] = news.find('p').text
            
            newsObj['detailsrc'] = news['href']
            
            newsContent.append(newsObj)
        
        
        #logger.debug( newsContent )
        
    except Exception as e:
        
        logger.warning( 'error : %s :' % e )
    
    finally:
        
        return newsContent


'''
首頁
'''
def index(request):
    
    title = 'NICE TO MEET YOU'
    pageName = 'NBA新聞'
    
    return render(request, 'news/index.html',
    {        
            'title': title,
            'pageName': pageName, 
    })
    
'''
1.抓取焦點新聞
'''
def demo_one(request):
    
    title = 'NICE TO MEET YOU'
    pageName = '1.抓取焦點新聞'
    
    newsContent = get_newsContent()
    
    return render(request, 'news/demo_1.html',
    {        
            'title': title,
            'pageName': pageName, 
            'newsContent' : newsContent,
    })
    
'''
2.使用 Django 設計恰當的 Model，并將所抓取新聞存儲至 DB。
'''
def demo_two(request):
    
    title = 'NICE TO MEET YOU'
    pageName = '2.使用 Django 設計恰當的 Model，并將所抓取新聞存儲至 DB。'
    
    newsContent = get_newsContent()
    
    newsDB = []
    #新增至資料庫
    for news in newsContent :
        
        newsDB.append( News.objects.get_or_create(**news)[0] )
    
    return render(request, 'news/demo_2.html',
    {        
            'title': title,
            'pageName': pageName, 
            'newsDB' : newsDB,
    })
    
'''
3.使用 Django REST Framework 配合 AJAX 實現以下頁面：
        焦點新聞列表
        新聞詳情頁面
'''
def demo_three(request):
    
    title = 'NICE TO MEET YOU'
    pageName = '3.使用 Django REST Framework 配合 AJAX 實現以下頁面 : 焦點新聞列表、新聞詳情頁面'
    
    return render(request, 'news/demo_3.html',
    {        
            'title': title,
            'pageName': pageName, 
            
    })
    
'''
4.進階要求
        實現爬蟲自動定時抓取。
        每當抓取到新的新聞時立即通知頁面。
'''
def demo_four(request):
    
    title = 'NICE TO MEET YOU'
    pageName = '4.進階要求 : 實現爬蟲自動定時抓取、每當抓取到新的新聞時立即通知頁面'
    
    return render(request, 'news/demo_4.html',
    {        
            'title': title,
            'pageName': pageName, 
            
    })
    
    

