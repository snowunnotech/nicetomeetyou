import requests
from html.parser import HTMLParser

class myParser(HTMLParser):
    def __init__(self):
        state = 's0'


    def handle_starttag(self, tag, attrs):
        if self.state == 's1':
            if tag == 'dt':
                self.state = 's2'
        elif self.state == 's2':
            if tag = 'a':
                pass

        elif tag == 'div' and ('id', 'news_body') in attrs and ('class', 'box_body') in attrs:
            self.state ='s1'



def task():
    url = "https://nba.udn.com/nba/index?gr=www"
    page = requests.get(url)
    # print(page.text)
    p = myParser()
    p.feed(page.text)

    pass


if __name__ == '__main__':
    task()