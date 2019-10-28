from bs4 import BeautifulSoup
import requests
from .models import Stock
from django.http import Http404

def get_web_page(url):
    '''
    Try to get the target page with requests.
    '''
    res = requests.get(url=url)
    try:
        if res.status_code == 200:
            soup = BeautifulSoup(res.text)
            return soup
        else:
            raise (Http404('Wrong status code:', res.status_code))
            return None
    except TypeError:
        raise (Http404('Cannot Get Web Page'))
        return None
def create_save(url):
    '''
    Crawl the  page of news, save to DB.
    '''

    soup = get_web_page(url)
    soup.encoding = 'utf-8'
    soup.find('div', id='news_list_body')

    for d in soup.find('div', id='news_list_body').find_all('dt'):
        href = 'https://nba.udn.com/' + d.find('a').get('href')
        name = d.find('h3').text
        context_soup = get_web_page(href)
        # context = context_soup.find('div', id='story_body_content').get_text()
        con = []
        for n in context_soup.find('div', id='story_body_content').find_all('p'):
            con.append(n.get_text())
        con.remove(' Getty Imagesfacebooktwitterpinterest')
        con.remove('')

        # Check Exist
        if Stock.objects.filter(link=href).exists():
            return None
        else:
            Stock.objects.create(
                name=name,
                link=href,
                context=con,
            )