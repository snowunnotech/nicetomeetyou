import scrapy
from ..items import CrawlerItem
import datetime
from scrapy.exceptions import CloseSpider
from api.models import HotNews


# scrapy crawl nbaSpider
# scrapyd
# scrapyd-deploy
# curl http://localhost:6800/schedule.json -d project=crawler -d spider=spiders


class NbaSpider(scrapy.Spider):
    name = "nbaSpider"
    start_urls = [
        'https://nba.udn.com/nba/cate/6754/-1/newest/1',
    ]
    close_down = False
    def parse(self, response):
        for detail_page in response.css('div#news_list_body dl dt a::attr(href)').getall():
            detail_page = response.urljoin(detail_page)
            # check crawler page is already in db
            if len(HotNews.objects.filter(news_url=detail_page)) != 0:
                self.close_down = True
                break
            yield scrapy.Request(detail_page, callback=self.parse_detail)

        if not self.close_down:
            next_page = response.css('gonext a::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):
        item = CrawlerItem()
        item['title'] = response.css('div#story_body_content h1::text').get()
        item['news_url'] = response.url
        item['image_url'] = response.css('.photo_center a img::attr(data-src)').get()
        post_date = response.css('div.shareBar__info--author span::text').get()
        post_date = datetime.datetime.strptime(post_date, '%Y-%m-%d %H:%M')
        item['post_date'] = post_date
        item['content'] = "".join(response.css('div#story_body_content span p *::text').getall()[4:])
        yield item

