from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup
import requests
import datetime

root = "https://nba.udn.com/nba/index"


def parse_content(content_link):
    content = requests.get(content_link).content.decode("UTF-8")
    soup = BeautifulSoup(content, features="lxml")
    content_span = soup.find("div", {"id": "story_body_content"}).find_all("p")
    time_source = soup.find("div", {"class": "shareBar__info--author"})
    post_time,source = time_source.span.contents[0],time_source.contents[1]
    post_time = datetime.datetime.strptime(post_time,"%Y-%m-%d %H:%M")
    content = []
    for s in content_span:
        content += [i for i in s.contents if isinstance(i, str)]
    content = "".join(content)
    return {"content":content,"source":source,"post_time":post_time}


def parse_article(item):
    parse_result = parse_content("https://nba.udn.com" + item.a.attrs["href"])
    parse_result.update(title = item.h3.contents[0])
    return parse_result

def get_current_news():
    text = requests.get(root).content.decode("UTF-8")
    soup = BeautifulSoup(text, features="lxml")
    all_news = soup.find("div", {"id": "news_body"}).find_all("dt")
    news = []
    for n in all_news:
        if 'ads' not in n.attrs.get('class', []):
            news.append(parse_article(n))
    return news


if __name__ == "__main__":
    news = get_current_news()
    for n in news:
        print(n)