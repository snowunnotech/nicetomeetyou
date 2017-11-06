#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:01:36 2017

@author: wayne17
"""

import requests
from bs4 import BeautifulSoup
host = "https://nba.udn.com"
url = "https://nba.udn.com/nba/index?gr=www"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Referer': 'https://academic.microsoft.com/',
        'Connection': 'keep-alive'
    }
response = requests.get(url, headers=headers).text
#f = open("tt.html","w")
#f.write(r.text)
#f.close
soup = BeautifulSoup(response,"lxml")
title_divs = soup.find("div", { "id" : "news_body" })
title, content, href, pic = "", "", "", ""
results=[]
for news in title_divs.find_all("dt"):
    title = news.find("h3").text.strip()
    content = news.find("p").text.strip()
    href = news.find("a")["href"]
    pic = news.find("img")["src"]
    results.append({"title": title, "content": content, "href": href, "pic": pic})
print(results)