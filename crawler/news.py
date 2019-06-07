""" This modules contains the class for parser the text """

from bs4 import BeautifulSoup as bs

class News:

    def __init__(self):
        self.title = None
        self.datetime = None
        self.content = None
