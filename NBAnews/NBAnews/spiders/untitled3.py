#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:09:34 2019

@author: rex
"""
import requests
from bs4 import BeautifulSoup as soup

start_urls = "https://nba.udn.com/nba/cate/6754"
domain = "https://nba.udn.com"

html = requests.get(start_urls)
res = soup(html.text,'html.parser')

news_list = res.select("#news_list_body")[0]
titles = news_list.select("h3")
links = news_list.select("a")      

for title in titles:
    print(title.text)
    
for link in links:
    print(domain + link["href"])
    

url = "https://nba.udn.com/nba/story/6780/3933583"
html = requests.get(url)
res = soup(html.text,'html.parser')

title = res.select(".story_art_title")[0].text
time = res.select(".shareBar__info--author")[0].select("span")[0].text
contents = res.select("#story_body_content")[0].find_all("p")[1:]
image = res.select('img[title="Getty Images"]')[0]["data-src"]
                      
all_content = ""
for content in contents:
    all_content += content.text
    
print(type(title))
print(type(all_content))
print(type(time))
print(type(image))
