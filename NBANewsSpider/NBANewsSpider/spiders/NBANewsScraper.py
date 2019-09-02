import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from NBANewsSpider.items import NbanewsItem

import os
from datetime import datetime

class NBANewsSpider(scrapy.Spider):
	name = 'NBANewsSpider'
	start_urls = ['https://nba.udn.com/nba/index?gr=www']
	
	def parse(self, response):
		ImgSaveDir = '/home/psyman/WorkSpace/nicetomeetyou/NBAHotNewsSite/NBAHotNewsApp/static/'
		BaseUrl = 'https://nba.udn.com'
		NewsXPath = '//div[@id="news_body"]/dl/dt/a'
		HotNewsList = response.xpath(NewsXPath).getall()

		for HotNews in HotNewsList:
			NewsSelector = Selector(text=HotNews)
			NewsDetailUrlXPath = '//a/@href'
			NewsTitleXPath = '//a/h3/text()'
			NewsImageXPath = '//a/span/img/@src'
			
			HotNewsItem = NbanewsItem()
			
			NewsTitle = NewsSelector.xpath(NewsTitleXPath).get()
			HotNewsItem["NewsTitle"] = NewsTitle

			NewsImageUrl = NewsSelector.xpath(NewsImageXPath).get()
			if NewsImageUrl is not None and 0 < len(NewsImageUrl) and 'jpg' in NewsImageUrl:
				ImgUrlStartIndex = NewsImageUrl.index('u=')+2
				ImgUrlEndIndex = NewsImageUrl.index('jpg')+3
				NewsImageUrl = NewsImageUrl[ImgUrlStartIndex:ImgUrlEndIndex]
				os.system("wget -nc " + NewsImageUrl + " -P " + ImgSaveDir)
				HotNewsItem["ImgFileName"] = NewsImageUrl.split('/')[-1]
			else:
				HotNewsItem["ImgFileName"] = ""

			NewsDetailUrl = BaseUrl+NewsSelector.xpath(NewsDetailUrlXPath).get()
			HotNewsItem["NewsId"] = NewsDetailUrl.split('/')[-1]
			
			NewsDetailPage = Request(NewsDetailUrl, callback=self.parseNewsDetail, meta={"HotNewsItem":HotNewsItem})

			yield NewsDetailPage

	def parseNewsDetail(self, response):
		BaseUrl = 'https://nba.udn.com'
		DetailContentXPath = '//div[@id="story_body_content"]'
		DetailContent = response.xpath(DetailContentXPath).get()
		HotNewsItem = response.meta["HotNewsItem"]
		
		ContentSelector = Selector(text=DetailContent)
		
		UpdateDateTimeXPath = '//div[@class="shareBar__info--author"]/span/text()'
		UpdateDateTime = datetime.strptime(ContentSelector.xpath(UpdateDateTimeXPath).get(), '%Y-%m-%d %H:%M')
		HotNewsItem["NewsUpdateDateTime"] = UpdateDateTime
		
		
		AuthorInfoXPath = '//div[@class="shareBar__info--author"]/text()'
		AuthorInfo = ContentSelector.xpath(AuthorInfoXPath).get()
		HotNewsItem["Author"] = AuthorInfo
		
		"""
		SearchUrlsXPath = '//p/a'
		ATags = ContentSelector.xpath(SearchUrlsXPath)
		if len(ATags) > 0:
			for ATag in ATags:
				SearchUrl = BaseUrl + ATag.attrib['href']
				#Source code hack, since the original attrib is rather a method that returns dict(root.attrib)
				ATag.root.attrib['href'] = SearchUrl
		"""
		
		NewsParagraphXPath = '//span/p//text()'
		NewsDetailParagraph = ""
		PTags = ContentSelector.xpath(NewsParagraphXPath).getall()
		for Paragraph in PTags:
			if 'Getty' in Paragraph or 'facebook' in Paragraph or 'twitter' in Paragraph or 'pinterest' in Paragraph:
				continue
			NewsDetailParagraph += Paragraph

		HotNewsItem["NewsDetailContent"] = NewsDetailParagraph
		
		yield HotNewsItem

