import scrapy
import pdb
import pytz
from datetime import datetime
from newsbot.items import NewsbotItem
from main.models import News

class NewsSpider(scrapy.Spider):
    name = "news"
    def start_requests(self):

        url = 'https://nba.udn.com/nba/index?gr=www'

        yield scrapy.Request(url=url, callback=self.parse_first)

    def parse_first(self, response):
        selector = scrapy.Selector(response)
        news_url_list = selector.xpath('//*[@id="news_body"]/dl//a/@href').extract()

        for news_url in news_url_list:

            # 如果 url 不為 null 且不為 javascript 語法
            if news_url and news_url != 'javascript:;':

                news_url = 'https://nba.udn.com' + news_url

                # 如果 url 在 DB 內沒出現過 (新的焦點新聞)
                if not News.objects.filter(post_url=news_url).exists():
                    
                    # 進入到要解析資料及預備 DjangoItem 的第二個 callback
                    yield scrapy.Request(
                                    news_url,
                                    callback=self.parse_second
                                )
                else:
                    pass
            else:
                pass

    def parse_second(self, response):
        selector = scrapy.Selector(response)

        # 解析資料
        news_url = response.url
        title = selector.css('.story_art_title::text').get()
        subtitle = selector.css('.shareBar__info--author::text').get()
        img_url = selector.xpath('//*[@id="story_body_content"]//img/@data-src').extract_first()
        post_date = datetime.strptime(selector.css(".shareBar__info--author span::text").get(), '%Y-%m-%d %H:%M')
        create_date = datetime.now()
        p_list = selector.css('#story_body_content > span > p ::text').getall() 
        p_list = [ x for x in p_list if x not in (' Getty Images', 'facebook', 'twitter', 'pinterest')]
        context = "".join(p_list)
        
        news = NewsbotItem(
                    title=title,
                    subtitle=subtitle,
                    context=context,
                    post_url=news_url,
                    img_url=img_url,
                    post_date=post_date,
                    create_date=create_date
                )

        yield news
