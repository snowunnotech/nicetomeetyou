import requests
from bs4 import BeautifulSoup

# Crawl first ten news
def get_data():
    url = 'https://nba.udn.com/nba/news/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # List of first ten news
    news_list = soup.find('div', attrs={'id': 'news_list_body'}).dl.findAll('dt')
    
    # Put data in python list
    link = ['https://nba.udn.com' + elem.a.get('href') for elem in news_list]
    pre_img_link = [elem.a.span.img.get('data-src') for elem in news_list]
    title = [elem.a.h3.text for elem in news_list]
    time = [elem.a.b.text for elem in news_list]
    preview = [elem.a.p.text for elem in news_list]
    
    # Initailize 'img_link' and 'paragraph'
    img_link = [0 for i in range(len(link))]
    paragraph = [0 for i in range(len(link))]

    # Crawl detail of each news
    for i in range(len(link)):
        res = requests.get(link[i])
        soup = BeautifulSoup(res.text, 'html.parser')

        # Get paragraphs (First two span tags are not what we want)
        story = soup.find('div', attrs={'id': 'story_body_content'}).findAll('span')[2].findAll('p')

        # story[0] contains image.
        img_link[i] = story[0].figure.a.img.get('data-src')

        # Join '\n' to be more readable in further HTML.
        content = [elem.text for elem in story[1:]]
        content = '\n'.join(content)

        paragraph[i] = content

    # Return a dictionary. 
    context = {
        'link': link,
        'pre_img_link': pre_img_link,
        'title': title,
        'time': time,
        'preview': preview,
        'img_link': img_link,
        'paragraph': paragraph,
    }    
    
    return context