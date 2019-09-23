from .models import News
from bs4 import BeautifulSoup
import requests
from collections import defaultdict

def crawl_news(url):
# url = 'https://nba.udn.com/nba/index?gr=www'

    source_code = requests.get(url).content
    soup = BeautifulSoup(source_code, 'html.parser')

    total_news = []

    web_url = 'https://nba.udn.com'

    for box in soup.select('#wrapper .box'):
        if box.select_one('.box-title'):
            if box.select_one('.box-title').text.startswith('焦點新聞'):
                for block in box.select('.box_body'):
                    for news in block.select('dt'):
                        hotnews = defaultdict()
                        if news.select('a span'):

                            hotnews['img'] = news.select_one('a span img')['src']
                            hotnews['full_url'] = web_url + news.select_one('a')['href']
                            hotnews['title'] = news.select_one('a h3').text
                            hotnews['content'] = news.select_one('a p').text

                            total_news.append(hotnews)

    # print(total_news)
    return total_news

def save(latest_news):
    if latest_news:
        for data in latest_news:

            News.objects.create(content=data['content'], title=data['title'], page_url=data['full_url'], img_url=data['img'])

# if __name__ == "__main__":
#     crawl_news("https://nba.udn.com/nba/index?gr=www ")
