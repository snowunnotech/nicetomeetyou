from html.parser import HTMLParser

class TopNewsParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__state = 's0'
        self.newsUrlList = []

    def handle_starttag(self, tag, attrs):
        if self.__state == 'mainbar' and tag == 'dt' and ('class', 'ads') not in attrs:
            self.__state = 'get_url'
        elif self.__state == 'get_url' and tag == 'a':
            self.newsUrlList.append(attrs[0][1])
            self.__state = 'mainbar'
        elif tag == 'div' and ('id', 'mainbar') in attrs:
            self.__state = 'mainBar'
        elif tag == 'div' and ('id', 'sidebar') in attrs:
            self.__state = 's0'


class TopNewsDetailParser(HTMLParser):
    # class NewsDetail():
    #     def __init__(self, postId, title, imgUrl, pageUrl):
    #         self.postId = postId
    #         self.title = title
    #         self.imgUrl = imgUrl
    #         self.pageUrl = pageUrl

    def __init__(self):
        HTMLParser.__init__(self)
        self.__state = 's0'
        self.title = ''
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

if __name__ == '__main__':
    import requests
    url = 'https://nba.udn.com/nba/story/6780/3464821'
    page = requests.get(url)
    p = TopNewsDetailParser()
    # print(page.text)
    p.feed(page.text)
    print(p.html)
