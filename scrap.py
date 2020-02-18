import requests
from bs4 import BeautifulSoup
import unicodedata
from datetime import datetime
urls = []

def get_response(url):
    try:
        res = requests.get(url, stream=True)
        return res.content
    except:
        return None
def prepare_soup(url):
    '''
    given a url string
    return soup made by BeaurifulSoup
    '''
    raw_html = get_response(url)
    #prepare soup for parsing
    soup = BeautifulSoup(raw_html, 'html.parser')
    return soup

def extract_domain(url):
    '''
    given url as string
    remove any character that is beyond '.com'
    return  a new url that contains only www.domain.com
    '''
    pos = url.rfind('.com')
    size = len('.com')
    end = pos + size
    return url[:end]

def get_list_of_url(soup, url):
    '''
    given a soup and url as string
    parse the html of the homepage to extract links in hot news
    return a list of links as string
    '''
    #find tag of news_body
    news_body = soup.find(id="news_body")
    #find anchor tag of news_body
    news = news_body.findChildren("a")
    #save get link from anchor and store the link
    links = []
    domain_url = extract_domain(url)
    for new in news:
        links.append(domain_url + new.attrs['href'])
    return links

def testLink():
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    print('===test get_list_of_url===')
    for link in links:
        print(link)

def testDuplicateLink():
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    #simulate database storage
    urls.extend(links)
    #accidentally request twice on the same page
    links = get_list_of_url(soup, url)
    print('===testDuplicateLink===')
    for link in links:
        if link not in urls:
            print(link)
        else:
            print(f"{link} is duplicated")



def extract_content(soup):
    '''
    given a soup
    return content of article as string
    '''
    tags = soup.find(id="story_body_content").findChildren('p')
    paragraphs = []
    #find out value <figcaption>
    for tag in tags:
        #get rid off p tag that has child of figure
        if tag.figure == None:
            paragraphs.append(tag.getText())
    return "".join(paragraphs)

def testContent():
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    for link in links:
        soup = prepare_soup(link)
        print(extract_content(soup))

def extract_title(soup):
    '''
    given a soup
    return title of the article as string
    '''
    tags = soup.find(id="story_body_content").findChildren('h1')
    return tags[0].getText()

def test_extract_title():
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    print("===start text_extract_title===")
    for link in links:
        soup = prepare_soup(link)
        print(extract_title(soup))


def get_time(soup):
    '''
    given a soup
    return time of the article as string
    '''
    tag = soup.find("div", {"class":"shareBar__info--author"}).find("span")
    date_string = tag.getText()
    date = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    return date

def test_get_time():
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    print('===start test get_time===')
    for link in links:
        soup = prepare_soup(link)
        print(get_time(soup))

def get_article_attribute(soup):
    '''
    given a soup
    return article information: reporter, type, office. The value of each is string
    '''
    tag = soup.find("div", {"class":"shareBar__info--author"})
    tag.find('span').extract()
    text = unicodedata.normalize('NFKC', tag.get_text())
    list_of_detail = text.split('/')
    article_attr = {}
    for detail in list_of_detail:
        if '記者' in detail:
            article_attr['reporter'] = detail.strip()
        elif '報導' in detail:
            article_attr['type'] = detail.strip()
        else:
            article_attr['office'] = detail.strip()
    return article_attr

def test_get_article_attribute():
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    for link in links:
        soup = prepare_soup(link)
        article = get_article_attribute(soup)
        print("===article get_article_attribute===")
        for key in article:
            print(key,': ', article.get(key, 'None'))

def main():
    #testDuplicateLink()
    #testLink()
    #testContent()
    #test_extract_title()
    test_get_time()
    #test_get_article_attribute()


if __name__ == "__main__":
    main()