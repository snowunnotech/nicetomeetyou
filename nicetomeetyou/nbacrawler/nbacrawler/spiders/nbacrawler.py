import scrapy
from nbacrawler.items import NbacrawlerItem


class NewsSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index']

    def parse(self, response):
        def parse_post(response):
            post = NbacrawlerItem()
            post['post_url'] = response.url
            post['post_id'] = response.url.split('/')[-1]
            post['timestamp'] = response.css('div.shareBar__info--author span::text').extract_first()
            post['reporter'] = response.css('div.shareBar__info--author::text').extract_first()
            post['image_url'] = response.css('figure img::attr(data-src)').extract_first()
            post['post_title'] = response.css('h1::text').extract_first()
            post['post_content'] = ''.join(response.css('div#story_body_content span p *::text').extract()[4:])

            post.save()
            yield post

        post_urls = response.css('div#news_body dt a::attr(href)').extract()
        for url in post_urls:
            yield scrapy.Request('https://nba.udn.com' + url, callback=parse_post)
