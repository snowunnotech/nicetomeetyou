# coding=utf8
import os
import requests
from bs4 import BeautifulSoup
import django

#-------------------全域變數宣告--------------------
title = ""
time = ""
content = ""
useimg = ""
#--------------------爬蟲區-------------------------

def get_news_data(home_url,nba_url):

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba.settings')
    django.setup()
    from news.models import newscatch

    web_data = requests.get(nba_url) #----主頁抓

    if web_data.status_code == requests.codes.ok:
        nbasoup = BeautifulSoup(web_data.text, 'html.parser')
        nbanews = nbasoup.select('#news_body dl dt a')
   
        for news in nbanews:
            title = news.find('h3').string #----主頁抓標題
        
            print (title)
            report_url =  (home_url+news.get("href"))

            nba_url_report = requests.get(report_url)
            nba_url_report_soup = BeautifulSoup(nba_url_report.text, 'html.parser')

            img_report = nba_url_report_soup.select('figure a img') #----抓首圖
            for img_content in img_report:
                useimg = img_content.get('data-src')
                print (useimg)

            time_report = nba_url_report_soup.select('.shareBar__info .shareBar__info--author span') #----抓時間
            for time_f in time_report:
                time = time_f.text
                print (time)

            nba_report = nba_url_report_soup.select('#story_body_content span p')#----抓內文喔
            content = ''
            for report_content in nba_report:
                #content = report_content.text
            
                if len(report_content) == 0 :
                    pass
                elif 'twitter' in report_content.text:
                    pass     
                else:  
                    content += report_content.text  
                    print (content)

            if newscatch.objects.filter(time=time):
                pass
            else:
                inputdb = newscatch.objects.create(title=title, time=time, cotent=content, img = useimg)
                             
if __name__=="__main__":
 
    home_url = 'https://nba.udn.com'
    nba_url = 'https://nba.udn.com/nba/index?gr=www'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba.settings')
    django.setup()
    from news.models import newscatch

    get_news_data(home_url,nba_url)

        
            

        
        
        
            
        
      


