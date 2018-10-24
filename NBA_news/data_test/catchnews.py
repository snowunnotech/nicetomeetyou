# coding=utf8
import requests
from bs4 import BeautifulSoup

#-------------------主連接區-----------------------

home_url = 'https://nba.udn.com'
nba_url = 'https://nba.udn.com/nba/index?gr=www'

#-------------------全域變數宣告--------------------
title = ""
time = ""
report_content = ""

#--------------------爬蟲區-------------------------
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
        for time in time_report:
            print (time.text)

        nba_report = nba_url_report_soup.select('#story_body_content span p')#----抓內文喔
        for report_content in nba_report:
            if len(report_content) == 0 :
                pass
            else:    
                print (report_content.text)
        
        
            

        
        
        
            
        
      


