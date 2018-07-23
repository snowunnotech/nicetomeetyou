import lxml
from bs4 import BeautifulSoup

import requests

class NBACrawler:

    def __init__(self):
        self._base_url = "https://nba.udn.com"
        index_url = f"{self._base_url}/nba/index?gr=www"
        self.main_parser(index_url)

    @staticmethod
    def get_soup(url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    def main_parser(self, index_url):
        soup = self.get_soup(index_url)

        for news_html in soup.find(id="mainbar").find(id="news_body").find_all("dt"):
            story_path = news_html.find("a")["href"]
            story_url = f"{self._base_url}{story_path}"
            image_url = news_html.find("img")["src"]
            title = news_html.find("h3").text
            story_datetime, story_author, story_content, video_url = self.story_parser(story_url)
            print(f"story_url: {story_url}\n"
                f"image_url: {image_url}\n"
                f"title: {title}\n"
                f"story_datetime: {story_datetime}\n"
                f"story_author: {story_author}\n"
                f"story_content: {story_content}\n"
                f"video_url: {video_url}\n")

    def story_parser(self, story_url):
        soup = self.get_soup(story_url)

        share_bar = soup.find(class_="shareBar__info--author")
        story_datetime = share_bar.find("span").text
        story_author = share_bar.text.replace(story_datetime, "")
        story_p_contents = soup.find(id="story_body_content").find_all("p")[1:]
        story_content = "\n".join([p_content.text for p_content in story_p_contents])
        video_url = soup.find(class_="video-container").find("iframe")["src"]
        return story_datetime, story_author, story_content, video_url

if __name__ == "__main__":
    NBACrawler()
