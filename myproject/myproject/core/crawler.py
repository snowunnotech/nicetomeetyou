
import requests
from bs4 import BeautifulSoup

# model
from myproject.core.models import New

# local module
from myproject.core.logging import Logger

class beautifulSoupResolver():
    '''
    Resolve beautiful soup and get news objects
    '''
    @classmethod
    def get_hot_new_from_block(cls, soup_element_dt=None, url_host='') -> 'New':
        '''
        Given beautiful soup object, and ti's also a dt element
        return New instance
        '''
        try:
            # This code depends on the web, create New instance
            new = New(**dict(
                url=url_host + (soup_element_dt.find('a')).attrs.get('href', ''),
                title_image_url=(soup_element_dt.find('img')).attrs.get('src', ''),
                title=(soup_element_dt.find('h3')).text,
                content=''
            ))
            cls.update_hot_new_deatil(news_instance=new)
            new.save()
            return new

        except Exception as e:
            Logger.log_exception(e)
            return None

    @classmethod
    def update_hot_new_deatil(cls, news_instance=None) -> 'New':
        news_page = requests.get(news_instance.url)
        soup = BeautifulSoup(news_page.text, 'html.parser')
        
        # This code depends on the web, find the detail content of New
        story_block = soup.find('div', id='story_body')
        story_lines = story_block.find_all('p')
        for idx, line in enumerate(story_lines):
            if idx > 0:
                print(line.text)
                news_instance.content += '%s\n' % line.text

        print()

class simpleCrawler():
    PROTOCOL = 'https'
    HOST = 'nba.udn.com'
    HOME = '/nba/index?gr=www'

    @classmethod
    def URL(cls, url=None):
        return f'{cls.PROTOCOL}://{cls.HOST}{url or cls.HOME}'

    @classmethod
    def run(cls):
        raw_data = requests.get(cls.URL())
        soup = BeautifulSoup(raw_data.text, 'html.parser')
        
        # get hot news
        hot_news_block = soup.find('div', id='news')
        hot_news = hot_news_block.find_all('dt')
        hot_news = list(
            # remove advertisement
            filter(lambda new: False if str(new.attrs.get('class')).find('ads') > -1 else True, hot_news)
        )
        
        news_instances = [
            beautifulSoupResolver.get_hot_new_from_block(soup_element_dt=new_block, url_host=f'{cls.PROTOCOL}://{cls.HOST}') 
            for new_block in hot_news
        ]
        news_instances = list(filter(lambda element: False if element is None else True, news_instances))

        print(f'News count: {len(news_instances)}')
        print('Check news content')
        for new in news_instances:
            print('### %s ###\n' % new.title)
            print('### %s ###\n' % new.url)
            print('### %s ###\n' % new.title_image_url)
            print(new.content, '\n')

        return True
