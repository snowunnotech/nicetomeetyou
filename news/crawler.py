import requests
from bs4 import BeautifulSoup
from models import NewsPost

base_url = "https://nba.udn.com/"
home_url = base_url + "nba/index?gr=www"
res = requests.get(home_url)
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.find(id='news_body').find_all('dt'):
    story_title = news.find('h3').text
    story_path = news.find('a')['href']
    story_url = base_url + story_path
    pic_url = news.find('img')['src']

    news_data = [story_title, pic_url]

    soup_story = BeautifulSoup(requests.get(story_url).text, 'html.parser')
    [news_data.append(para.text) for para in soup_story.find_all('p')[\
        1:] if len(para.text) is not 0]
    news_data = NewsPost(title=news_data[0], photo_url=news_data[1], para1=news_data[2],\
                         para2=news_data[3], para3=news_data[4], para4=news_data[5])
    news_data.save()
