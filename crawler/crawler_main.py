# -*- coding: utf-8 -*-

from crawler.utils.common import catch_page_by_soup
from crawler.utils.news import get_total_pages, get_news_list, catch_news
from crawler.utils.website import import_to_website

cooldown_time = 1

def start_crawler() :
    # 先進入焦點新聞
    url = 'https://nba.udn.com/nba/cate/6754/-1/newest/'

    # 抓取首頁，以取得所有頁數
    homepage_soup = catch_page_by_soup(url, cooldown_time)

    total_pages = get_total_pages(homepage_soup)
    total_pages = total_pages + 1

    def catch_news_page_by_page(total_pages):
        for page in range(1, total_pages):
            base_url = 'https://nba.udn.com/nba/cate/6754/-1/newest/'
            sub_url = base_url + str(page)
            sub_soup = catch_page_by_soup(sub_url, cooldown_time)

            news_url_list = get_news_list(sub_soup)
            for news_url in news_url_list:
                news_soup = catch_page_by_soup(news_url, cooldown_time)
                news = catch_news(news_soup, news_url)

                # 抓完新聞後通過news_import接口上傳至數據庫
                import_to_website(news)

    catch_news_page_by_page(total_pages)

