import scrapy


class TopNewsBotItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    data = scrapy.Field()
