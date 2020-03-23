from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from .models import NbaSpider
from django.http import JsonResponse


def index(request):
    return render(request, 'news/index.html')


def get_news_list(request):
    return JsonResponse(crawler(), safe=False)


def news_detail(request):
    return None


def crawler():
    url = 'https://nba.udn.com/nba/index?gr=www'
    s = construct_soup(url)
    news_urls = get_news_urls(s, get_base_domain(url))
    news_list = []
    for news in news_urls:
        article = get_news_detail(news)
        news_list.append(article)
        # Debugging
        insert_news(article)

    return news_list


def construct_soup(url: str):
    raw_html = get_response(url)
    soup = BeautifulSoup(raw_html, 'html.parser')
    return soup


def get_response(url: str):
    try:
        res = requests.get(url, stream=True)
        return res.content
    except:
        return None


def get_news_urls(soup: BeautifulSoup, base_domain: str):
    news_links = soup.find(id="news_body").findChildren("a")
    links = []
    for link in news_links:
        links.append(base_domain + link.attrs['href'])

    return links


def get_news_detail(news_links: str):
    news_detail = {}
    soup = construct_soup(news_links)
    news_detail["date_time"] = get_news_date_time(soup)
    news_detail["author"] = get_news_author(soup)
    news_detail["title"] = get_news_title(soup)
    news_detail["content"] = get_news_content(soup)
    news_detail["url"] = news_links

    return news_detail


def get_news_date_time(soup: BeautifulSoup):
    tag = soup.find("div", {"class": "shareBar__info--author"}).find("span")
    news_publish_date_time = datetime.strptime(tag.getText(), '%Y-%m-%d %H:%M')

    return news_publish_date_time


def get_news_author(soup: BeautifulSoup):
    tag = soup.find("div", {"class": "shareBar__info--author"})
    tag.span.clear()
    return tag.text


def get_news_title(soup: BeautifulSoup):
    return soup.find(id="story_body_content").find("h1").getText()


def get_news_content(soup: BeautifulSoup):
    content = soup.find(id="story_body_content").find("p").getText()
    return content


def get_base_domain(url: str):
    return url[:url.rfind('.com')+4]


def insert_news(news):
    created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M')

    m = NbaSpider(
        created_at=str(created_at),
        publish_at=news['date_time'],
        author=news['author'],
        title=news['title'],
        content=news['content'],
        news_url=news['url']
    )
    m.save()
