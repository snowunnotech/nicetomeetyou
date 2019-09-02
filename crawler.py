import scrapy
from bs4 import BeautifulSoup
from getnews.models import hotnew


class NbaCrawler(scrapy.Spider):
	name = 'nba'
	start_urls = ['https://nba.udn.com/nba/index?gr=www']
	
	def parse(self, response):
		res = BeautifulSoup(response.body)
		a = res.select('.box_body')
		
		for news in a[0].select('dt'):
			link = 'https://nba.udn.com' + news.find('a')['href']
			id = link.split('/')[6]
			title = news.select('h3')[0].text
			
			obj, created = hotnew.objects.get_or_create(new_id = id, new_title = title, new_link = link)
			print(link + '\n' + title)