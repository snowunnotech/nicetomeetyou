from scrapy.spiders import CrawlSpider
from api.models import News
import scrapy, datetime
from SpiderBot.items import NBANewsItem

class NBASpider(CrawlSpider):
    name = 'NBANews'
    start_urls = ['https://nba.udn.com/nba/index?gr=www']
    def parse(self, response):
        for item in response.css('#mainbar #news #news_body'):
            for dt in item.css('dt:not(.ads)'):
                url = response.urljoin(dt.css('a::attr(href)')[0].extract())
                yield scrapy.Request(url, callback=self.ParseNewsContent)

    def ParseNewsContent(self, response):
        for news in response.css('#mainbar #story #story_body #story_body_content'):
            Title = news.css('.story_art_title ::text')[0].extract()
            NewsPostDatetime = news.css('.shareBar__info .shareBar__info--author span ::text')[0].extract()
            NewsPhoto = news.css('.photo_center a img::attr(data-src)')[0].extract()
            NewsContent = ''
            for Span in news.css('span p'):
                if 'facebook' not in Span.css('::text').extract() and len(Span.css('::text').extract()) > 0:
                    for conetent in Span.css('::text').extract():
                        NewsContent += conetent
            item = NBANewsItem()
            item['Title'] = Title
            item['CreateAt'] = datetime.datetime.strptime(NewsPostDatetime, '%Y-%m-%d %H:%M') - datetime.timedelta(hours=8)
            item['Content'] = NewsContent
            item['Url'] = response.url
            if not News.objects.filter(Url=item['Url']).exists():
                yield item
            else:
                pass