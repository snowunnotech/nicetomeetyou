import asyncio
import async_timeout

import aiohttp
import lxml
import requests
from bs4 import BeautifulSoup
import cgi

from news.models import News

class NBACrawler:

    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main(loop))

    async def main(self, loop):
        base_url = "https://nba.udn.com"
        index_url = "{base_url}/nba/index?gr=www".format(base_url=base_url)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        soup = self.get_soup(index_url)

        news_html_list = soup.find(id="mainbar").find(id="news_body").find_all("dt")

        async with aiohttp.ClientSession(loop=loop, headers=headers, conn_timeout=5 ) as client:
            tasks = [self.main_parser(client, base_url, news_html) for news_html in news_html_list]
            await asyncio.gather(*tasks)

    @staticmethod
    def get_soup(url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    async def main_parser(self, client, base_url, news_html):
        print("NBA Crawler start")

        story_path = news_html.find("a")["href"]
        story_url = "{base_url}{story_path}".format(base_url=base_url, story_path=story_path)
        image_url = news_html.find("img")["src"]
        title = news_html.find("h3").text
        with async_timeout.timeout(10):
            async with client.get(story_url) as response:
                assert response.status == 200
                html = await response.text()
                soup = BeautifulSoup(html ,'lxml')
                story_datetime, story_author, story_content, video_url = self.story_parser(soup)
                news_info = { 
                    "author": story_author, 
                    "datetime": story_datetime, 
                    "title": title, 
                    "image_url": image_url, 
                    "story_url": story_url, 
                    "content": story_content, 
                    "video_url": video_url
                }
                for key in news_info.keys():
                    if key == "datetime":
                        continue
                    news_info[key] = cgi.escape(news_info[key], quote=True)
                if not News.objects.filter(datetime=news_info["datetime"], title=news_info["title"]).exists():
                    News.objects.create(**news_info)
                return await response.release()

    def story_parser(self, soup):
        share_bar = soup.find(class_="shareBar__info--author")
        story_datetime = share_bar.find("span").text
        story_author = share_bar.text.replace(story_datetime, "")
        story_p_contents = soup.find(id="story_body_content").find_all("p")[1:]
        story_content = "\n".join([p_content.text for p_content in story_p_contents])
        try:
            video_url = soup.find(class_="video-container").find("iframe")["src"]
        except:
            video_url = ""
        return story_datetime, story_author, story_content, video_url

if __name__ == "__main__":
    NBACrawler()
