import json
import requests
from bs4 import BeautifulSoup

def get_latest_news():
    rtn_news = list()
    website_url = "https://nba.udn.com/nba/index?gr=www"
    website_basic_url = "https://nba.udn.com"

    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('div', {"id": "news_body"})
    articles = table.find_all('dt')

    for article in articles:
        title = article.find('h3')
        href = article.find('a', href=True)
        if not title or not href:
            continue
        #crawler for more information of article
        article_details = get_article_details(website_basic_url + href['href'])
        rtn_news.append(article_details)

    rtn_news = rtn_news[::-1] #let news from old to new
    return rtn_news

def get_article_details(article_url):
    rtn_details = dict()
    response = requests.get(article_url)

    soup = BeautifulSoup(response.text, 'lxml')
    article_details_text = soup.find("script", type='application/ld+json').text
    article_details = json.loads(article_details_text)

    rtn_details['title'] = article_details['headline']
    rtn_details['url'] = article_url
    original_crawled_content = soup.select("div[id='story_body_content']\
                                            span p")
    article_content = get_article_content(original_crawled_content)
    rtn_details['content'] = article_content
    rtn_details['image_url'] = article_details['thumbnailUrl']
    rtn_details['published_time'] = article_details['datePublished']

    return rtn_details

def get_article_content(original_crawled_content):
    article_content = ""
    #slice for filter the 美聯社、Facebook...text
    for span in original_crawled_content[2:]:
        span = span.text
        if span:
            article_content += span

    return article_content
