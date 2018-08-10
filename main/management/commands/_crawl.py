from bs4 import BeautifulSoup
from datetime import datetime
import requests

from main.models import News


HOST = 'https://nba.udn.com'
URL = HOST + '/nba/index?gr=www'


def get_web_page(url):
    '''
    Try to get the target page with requests.
    '''
    try:
        resp = requests.get(url=url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            return soup
        else:
            print('Wrong status code:', resp.status_code)
            return None
    except TypeError:
        print('Cannot get web page')
        return None


def create_and_save(url):
    '''
    Crawl the detail page of news, clean the data and save to DB.
    '''
    soup = get_web_page(url)
    # check if the news exists
    if News.objects.is_new(url=url):
        title = soup.find("h1", "story_art_title").text
        pub_time = soup.find("div", "shareBar__info--author").span.text
        pub_time = datetime.strptime(pub_time, '%Y-%m-%d %H:%M')
        crawl_time = datetime.now()
        paragraphs = soup.find("div", id="story_body_content").find_all("span")[2].find_all("p")

        # clean the content data
        content = ''
        for paragraph in paragraphs:
            if paragraph.find("figure"):
                continue
            content += paragraph.text

        News.objects.create(
            url=url,
            title=title,
            pub_time=pub_time,
            crawl_time=crawl_time,
            content=content
        )


def crawl():
    '''
    Find the target urls, and run the crawling process.
    '''
    soup = get_web_page(URL)
    dts = soup.find("div", id="news").find_all("dt")
    for dt in dts:
        href = dt.a['href']
        create_and_save(url=HOST+href)
