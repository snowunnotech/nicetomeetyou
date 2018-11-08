from html.parser import HTMLParser


class TopNewsParser(HTMLParser):

    class News:
        def __init__(self, post_id, title, img_url, page_url):
            self.postId = post_id
            self.title = title
            self.imgUrl = img_url
            self.pageUrl = page_url

    def __init__(self):
        HTMLParser.__init__(self)
        self.__state = 's0'
        self.news_list = []
        self.__title = ''
        self.__img_url = ''
        self.__page_url = ''

    def handle_starttag(self, tag, attrs):
        if self.__state == 'mainbar' and tag == 'dt' and ('class', 'ads') not in attrs:
            self.__state = 'get_url_tag'
        elif self.__state == 'get_url_tag' and tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.__page_url = attr[1]
                    break
            self.__state = 'get_img_tag'
        elif self.__state == 'get_img_tag' and tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.__img_url = attr[1]
                    break
            self.__state = 'find_title'
        elif self.__state == 'find_title' and tag == 'h3':
            self.__state = 'get_title'
        elif tag == 'div' and ('id', 'mainbar') in attrs:
            self.__state = 'mainbar'
        elif tag == 'div' and ('id', 'sidebar') in attrs:
            self.__state = 'end'

    def handle_data(self, data):
        if self.__state == 'get_title':
            self.__title = data
            self.news_list.append(
                self.News(int(self.__page_url.split('/')[-1]),
                          self.__title,
                          self.__img_url,
                          self.__page_url))
            self.__state = 'mainbar'


class TopNewsDetailParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__state = 's0'
        self.html = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'style' or tag == 'ul':
            self.__state += '1'
        if self.__state == 's0' and tag == 'div' and ('class', 'shareBar__info--author') in attrs:
            self.__state = 'get_author'
        elif self.__state == 'get_detail':
            if tag == 'p':
                self.html += '<p>'
            elif tag == 'img':
                for attr in attrs:
                    if attr[0] == 'data-src':
                        self.html += '<img src=' + attr[1] + '>'
                        break

    def handle_data(self, data):
        if self.__state == 'get_author':
            self.html += '<p>' + data + '<p>'
        elif self.__state == 'get_detail':
            self.html += data

    def handle_endtag(self, tag):
        if tag == 'style' or tag == 'ul':
            self.__state = self.__state[:-1]
        if self.__state == 'get_author' and tag == 'div':
            self.__state = 'find_detail'
        elif self.__state == 'get_detail' and tag == 'p':
            self.html += '</p>'

    def handle_comment(self, data):
        if self.__state == 'find_detail' and data == ' art_body 內文 ':
            self.__state = 'get_detail'
        elif self.__state == 'get_detail' and data == '999':
            self.__state = 'end'


# parser testing
if __name__ == '__main__':
    import requests
    url = 'https://nba.udn.com/nba/story/6780/3464821'
    page = requests.get(url)
    p = TopNewsDetailParser()
    # print(page.text)
    p.feed(page.text)
    print(p.html)
