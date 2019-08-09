from news.models import News, NewsStory
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

nbaUrl = 'https://nba.udn.com/nba'


def create_or_update_in_news_table(news_array):
    for news in news_array:
        News.objects.update_or_create(
            title=news.title,
            defaults={
                'title': news.title,
                'imgUrl': news.imgUrl,
                'time': news.time,
                'url': news.url,
                'payload': news.payload
            }
        )


def create_or_update_in_newsStory_table(news_story_array):
    for newsStory in news_story_array:
        news_document = News.objects.get(title=newsStory.title)
        NewsStory.objects.update_or_create(
            parent=news_document,
            defaults={
                'fbLike': newsStory.fbLike,
                'author': newsStory.author,
                'payload': newsStory.payload,
                'vedioUrl': newsStory.vedioUrl,
                'imgUrl': newsStory.imgUrl
            }
        )


class New:
    def __init__(self, title, imgUrl, time, payload, url):
        self.title = title
        self.imgUrl = imgUrl
        self.time = time
        self.payload = payload
        self.url = url


class NewStory:
    def __init__(self, title, fbLike, author, imgUrl, payload, vedioUrl):
        self.title = title
        self.author = author
        self.fbLike = fbLike
        self.payload = payload
        self.imgUrl = imgUrl
        self.vedioUrl = vedioUrl


def soupNews(soup):
    news = soup.find('div', id='news')
    array = news.find_all('dt')
    results = []
    for element in array:
        if element.find('style'):
            break
        results.append(New(
            title=element.find('h3').string,
            imgUrl=element.find('img').get('src'),
            time=element.find('b').string,
            payload=element.find('p').string,
            url=nbaUrl + element.find('a').get('href')[4:]
        ))
    return results


def spider(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')


def soupNewsStory(soup, current_news):
    story = soup.find('div', id='story_body_content')
    payload = ''
    tag_p_array = story.find_all('p')
    for element in tag_p_array:
        payload += '\n' + ''.join(element.find_all(text=True))

    return NewStory(
        title=current_news.title,
        # fbLike=getFbLike(current_news.url),
        fbLike='none',
        author=story.select('div .shareBar__info--author')[0].get_text(),
        imgUrl=story.select('figure > a > img')[0].get('data-src'),
        payload=payload,
        vedioUrl=story.select('div .video-container > iframe')[0].get('src')
    )


def getFbLike(url):
    driver = webdriver.Chrome('news/chromedriver')
    driver.get(url)
    driver.switch_to_default_content()
    fb_like_url = driver.find_element_by_class_name('fb-like').find_element_by_tag_name('iframe').get_attribute('src')
    driver.close()

    soupFbLike = spider(fb_like_url)
    return soupFbLike.find('span', id='u_0_3').string


# news spider task per minutes
def news_spider():
    # get news
    soup = spider(nbaUrl)
    news = soupNews(soup)

    # get every news story
    newsStorys = []
    for current_news in news:
        testNewsStorySoup = spider(current_news.url)
        newsStorys.append(soupNewsStory(testNewsStorySoup, current_news))

    # create or update data in news table
    create_or_update_in_news_table(news)

    # create or update data in news story table
    create_or_update_in_newsStory_table(newsStorys)

    return 'OK'
