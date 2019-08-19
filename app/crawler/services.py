import scrapy
import requests
from django.apps import apps
# Set NBA site
base_url = 'https://nba.udn.com'

def CALL_SELECTOR(url):
    url = url
    res = requests.get(url=url)
    html = res.text
    sel = scrapy.Selector(text=html)
    return sel

# Crawl
def CRAW(url='https://nba.udn.com/nba/index?gr=www'):
    sel = CALL_SELECTOR(url)
    for quote in sel.css('#news_body'):
        news_dic = {
            'time': quote.css('b::text').getall(),
            'title': quote.css('h3::text').getall(),
            'intro': quote.css('p::text').getall(),
            'link': quote.css('a::attr(href)').getall(),
        }
    content_list = []
    counter = 0
    for link in news_dic['link']:
        url = base_url + link
        news_dic['link'][counter] = url
        counter += 1
        sel = CALL_SELECTOR(url)
        for quote in sel.css('#story_body_content'):
            print ('quote', quote)
            content = quote.css('p::text').getall()
            content = "".join(content)
            content_list.append(content)
    news_dic['content'] = content_list
    zip_news = zip(news_dic['time'], news_dic['title'], news_dic['intro'], news_dic['link'], news_dic['content'])

    return zip_news

def CHECK_EXIST(tuple_data):
    NBANewsInFocus = apps.get_model('crawler','NBANewsInFocus')
    title = tuple_data[1]
    news = NBANewsInFocus.objects.filter(title=title)
    if news.exists():
        return True
    else:
        return False

def SAVE_NEWS(tuple_data):
    NBANewsInFocus = apps.get_model('crawler','NBANewsInFocus')
    title = tuple_data[1]
    intro = tuple_data[2]
    link = tuple_data[3]
    content = tuple_data[4]
    new_news_obj = NBANewsInFocus.objects.create(
        title = title,
        intro = intro,
        link = link,
        content = content,
    )
    new_news_obj.save()
    news_id = new_news_obj.id
    return news_id


