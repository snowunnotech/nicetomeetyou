import requests
from bs4 import BeautifulSoup

url = 'https://nba.udn.com/nba/index?gr=www'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
domain = 'https://nba.udn.com'

for news in soup.find(id = 'news_body').find_all('a'):
    # print(domain + news.get('href'))
    news_content = requests.get(domain + news.get('href'))
    news_soup = BeautifulSoup(news_content.text, 'html.parser')

    title = news_soup.find(class_='story_art_title').text
    story_url = news_soup.find(property = 'og:url').get('content')
    date = news_soup.find(class_='shareBar__info--author').find('span').text
    source = news_soup.find(class_='shareBar__info--author').text.replace(date, '')
    content = ''.join(i.text for i in news_soup.find(id = 'story_body_content').find_all('p'))
    content = content.replace(' Getty Imagesfacebooktwitterpinterest', '')

    print(title)
    print(story_url)
    print(date)
    print(source)
    print(content)
