# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
def resolve_html(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def catch_page_by_soup(url, cooldown_time):
    try:
        # 顯示目前解析的網頁
        print('catch:', url)

        resp = requests.get(url)
        resp.encoding = 'utf-8'  # encoded with format utf-8 for chinese character
        soup = BeautifulSoup(resp.text, 'lxml')
    except Exception as e:
        print(e)
    finally:
        # 抓完休息一秒，避免被ban
        time.sleep(cooldown_time)
        return soup