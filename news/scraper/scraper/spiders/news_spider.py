import scrapy
from scraper.items import NBAnewsItem
class NewsSpider(scrapy.Spider):
  name = "spidy"
  start_urls = [
    "https://nba.udn.com/nba/index?gr=www"
  ]

  def parse(self,response):
    data = response.css("div#news_body")
    for href in data.css('a::attr(href)').getall():
      yield response.follow(href,self.parse_detail)
  def parse_detail(self,response):
    article = response.css('div#story_body_content')
    for a in article:
      item = NBAnewsItem()
      item['title'] = a.css("h1.story_art_title::text").getall()
      item['content'] = a.xpath("//p//text()").getall()
      yield item 
      