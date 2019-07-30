import requests
import re
from bs4 import BeautifulSoup
import json
import pymysql

def get_url(url):
    base = 'https://nba.udn.com/nba/story/'
    resp = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'})
    html = resp.text
    pat_url = '><a href="/nba/story/(.*?)"><span'
    urls =[ base+url for url in re.compile(pat_url).findall(html)[0:3]]
    return urls

def get_article(url):
    result={}
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'})
    html = resp.text
    pat_author = '<div class="shareBar__info--author"><span>\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}</span>(.*?).</div>'
    pat_date = '<span>(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})</span>'
    pat_title = '<h1 class="story_art_title">(.*?)</h1>'
    author = re.compile(pat_author).findall(html)
    date = re.compile(pat_date).findall(html)
    title = re.compile(pat_title).findall(html)
    soup = BeautifulSoup(html, 'html.parser')
    contents = [p.text.strip()+'\n' for p in soup.select('#story_body_content span p') if p.text.strip()]
    contents = ''.join(contents)

    result['title'] = title[0]
    result['author'] = author[0]
    result['date'] = date[0]
    result['content'] = contents
    return result

if __name__ == '__main__':
    target_url = 'https://nba.udn.com/nba/index?gr=www'
    url_list = get_url(target_url)
    result = [get_article(url) for url in url_list]
    # result_json = json.dumps(result,ensure_ascii=False)
    # with open('./output.json','w',encoding='utf-8') as file:
    #     file.write(result_json)
    conn = pymysql.connect(host='192.168.88.132',password='root',user='root',
                           port=3306,db='nba_focus')
    cursor = conn.cursor()
    # print(type(result[0]['title']))
    # print(result[0]['author'])
    # print(result[0]['content'])
    # print(result[0]['date'])
    sql = "insert into focus_entry (title,author,body,created_time,modified_time) values (%s, %s, %s,%s, %s)"
    for article in result:
        effect_row = cursor.execute(sql,(str(article['title']),str(article['author']),str(article['content']),str(article['date']),str(article['date'])))
        conn.commit()
    cursor.close()
    conn.close()