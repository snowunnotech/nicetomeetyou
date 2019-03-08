import sys

import requests
from bs4 import BeautifulSoup

from crawler.crawlerNewsPage import CrawlerNewsPage


class CrawlerNewsList:
    def __init__(self, page=1, endPage=1):
        self._page = page
        self._endPage = endPage + 1

    def run(self):
        for i in range(self._page, self._endPage):
            self.crawler(i)

    def crawler(self, page):
        url = 'https://nba.udn.com/nba/cate/6754/-1/newest/{}'
        url = url.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        news_list_body = soup.select('div#news_list_body')[0]
        aList = news_list_body.select('a')

        for a in aList:
            h3 = a.select('h3')
            title = h3[0].text
            url = a['href']
            print(url, title)
            CrawlerNewsPage(url)


if __name__ == '__main__':

    page = 1
    endPage = page
    if len(sys.argv) == 2:
        page = int(sys.argv[1])
    if len(sys.argv) == 3:
        endPage = int(sys.argv[2])

    crawlerNewsList = CrawlerNewsList(page, endPage)
    crawlerNewsList.run()

    # EX
    # python -m cralwer.crawlerNewsPage 1 2
