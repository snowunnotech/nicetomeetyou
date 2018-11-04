# -*- coding: utf-8 -*-
from crawler.utils.common import resolve_html

def get_total_pages(soup):
    _ = ''
    try:
        # 抓取特定標籤
        _ = soup.find_all('span', class_='total')
        # 取得文字
        _ = _[0].text
        # 去除多餘資訊
        _ = _.replace(u"共", '').replace(u"頁", '').strip()
    except Exception as e:
        print(e)
    finally:
        return int(_)

def get_news_list(soup):
    news_list = list()
    base_url = 'https://nba.udn.com'

    try:
        # 找到新聞列表
        list_body = soup.find_all('div', id='news_list_body')
        n_list = list_body[0].dl.children
        for item in n_list:
            a = item.a
            news_url = base_url + a.get('href')

            news_list.append(news_url)
    except Exception as e:
        print(e)
    finally:
        return news_list

def catch_news(soup, news_url):
    news = None
    try:
        title = soup.select('.story_art_title')[0].text
        shareBar = soup.select('.shareBar__info--author')[0]
        org_news_date = shareBar.span.text
        author = shareBar.text.replace(org_news_date, '')
        _ = str(soup.find_all('div', id='story_body_content')[0])
        content_soup = resolve_html(_)
        ps = content_soup.find_all('p')
        content = ""
        for p in ps:
            p = p.text.strip()
            content += p

        news = {'title': title,
                'author': author,
                'content': content,
                'org_news_date': org_news_date,
                'news_url': news_url}
    except Exception as e:
        print(e)
    finally:
        return news