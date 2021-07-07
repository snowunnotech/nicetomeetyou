import urlparse
import requests
import bs4
import sqlite3


def get_spec_html(url, spec_id):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return soup.find(id=spec_id)


def parsing_story(url, spec_id="story_body_content"):
    story_body = get_spec_html(url, spec_id)
    title = story_body.find("h1").get_text()  # title
    info_author = story_body.find("div", {"class": "shareBar__info--author"})  # info & author
    info = info_author.find("span").get_text()  # info
    author = info_author.get_text().replace(info, "")  # author
    paragraph = map(lambda p: p.get_text(), story_body.find_all("p"))  # paragraph
    story = "\n".join(paragraph)
    story = story.replace(story[:story.index("facebooktwitterpinterest")], "")
    story = story.replace("facebooktwitterpinterest", "").strip()  # story
    return info, author, title, story


class udn_nba_new:
    def __init__(self):
        self.base_url = "https://nba.udn.com/nba/index?gr=www"
        self.news = "news"
        self.news_list = "news_list"
        self.news_list_body = "news_list_body"

    def get_news_link(self):
        spec_html = get_spec_html(self.base_url, self.news)
        sub_url = spec_html.find("h1").find("a")["href"]
        return urlparse.urljoin(self.base_url, sub_url)

    def get_news_details_link(self):
        spec_html = get_spec_html(self.get_news_link(), self.news_list_body)
        join_urls = map(
            lambda sub_url: urlparse.urljoin(self.base_url, sub_url["href"]),
            spec_html.find_all("a")
        )
        return list(join_urls)


news = udn_nba_new()
news_links = news.get_news_details_link()
data = [parsing_story(url) for url in news_links]


conn = sqlite3.connect("../db.sqlite3")
try:
    query = """
    create table if not exists nba_news(
        info datetime,
        author varchar(100),
        title varchar(100),
        story varchar(100000)
    );
    """
    conn.execute(query)
    conn.commit()

    conn.executemany("insert into nba_news values(?, ?, ?, ?)", data)
    conn.commit()

finally:
    conn.close()
