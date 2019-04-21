import scrapy
from bs4 import BeautifulSoup



class NBASpider(scrapy.Spider):
    name = "nba"
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        domain_name = 'https://nba.udn.com'

        print()
        print()
        print()
        print("procesing....:" + response.url)
        print()

        # extract data using css
        news_titles = response.css('[id="news_body"] a h3').extract()
        news_links = response.css('[id="news_body"] a::attr(href)').extract()
        news_text = response.css('[id="news_body"] a p').extract()
        for i in range(len(news_titles)):
            print("Title: " + news_titles[i])
            print("URL: " + domain_name  + news_links[i])
            print("Text: " + news_text[i])

        row_data = zip(news_titles, news_text, news_links)
        for item in row_data:
            scraped_info = {
            'title': item[0],
            'text': item[1],
            'url': item[2],
            }
            yield scraped_info

        # extract data using xpath
        print()
        print()
        print()
