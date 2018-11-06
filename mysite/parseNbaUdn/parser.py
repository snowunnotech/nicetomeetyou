from html.parser import HTMLParser


class TopNewsParser(HTMLParser):
    class News():
        def __init__(self, postId, title, imgUrl, pageUrl):
            self.postId = postId
            self.title = title
            self.imgUrl = imgUrl
            self.pageUrl = pageUrl

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.__state = 's0'
        self.newsList = []
        self.__title = ''
        self.__imgUrl = ''
        self.__pageUrl = ''
        self.__baseUrl = url

    def handle_starttag(self, tag, attrs):
        if self.__state == 's1':
            if tag == 'dt':
                self.__state = 'get_url_tag'
        elif self.__state == 'get_url_tag' and tag == 'a':
            self.__pageUrl = attrs[0][1]
            self.__state = 'get_img_tag'
        elif self.__state == 'get_img_tag' and tag == 'img':
            self.__imgUrl = attrs[0][1]
            self.__state = 'get_title_tag'
        elif self.__state == 'get_title_tag' and tag == 'h3':
            self.__state = 'get_title_data'
        elif tag == 'div' and ('id', 'mainbar') in attrs:
            self.__state = 's1'
        elif tag == 'div' and ('id', 'sidebar') in attrs:
            self.__state = 's0'

    def handle_data(self, data):
        if self.__state == 'get_title_data':
            self.__title = data
            self.newsList.append(
                self.News(int(self.__pageUrl.split('/')[-1]),
                          self.__title,
                          self.__imgUrl,
                          self.__baseUrl + self.__pageUrl))
            self.__state = 's1'




