## import django 
import sys
import os
import django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawlnews.settings")
django.setup()

# import tools
import requests
from bs4 import BeautifulSoup
from main.models import News



# do the crawl
host = "https://nba.udn.com"
response = requests.get( host + "/nba/index?gr=www")
html = response.text
soup = BeautifulSoup(html, features="html.parser")
a_tags = soup.select("div#news_body dl > dt > a")

content = {
    "news" : [],
}

# store into db
for a_tag in a_tags :
    
    # get everything we need first
    news_dictionary = dict( zip(
        ["time", "title", "statement"], a_tag.stripped_strings
    ) )
    url_detail = a_tag.get("href")
    url_id = url_detail.split("/")[-1]
    image = a_tag.select_one("span.img-boxs img").get("src")

    # crawl another detail page
    Soup = BeautifulSoup( requests.get( host + url_detail ).text, features="html.parser")
    author = Soup.select_one("div#story_body_content div.shareBar__info--author")
    author_dictionary = dict( zip(
        ["author_time", "author"], author.stripped_strings
    ) )
    p_tags = Soup.select("div#story_body_content p:not(:has(div)):not(:empty)")
    body_content = "\n\n".join( map( lambda x: x.text, p_tags ) )
    
    # create model and save it
    news, created = News.objects.get_or_create(url_id=url_id)
    if created :
        news.url_detail = url_detail
        news.image = image
        news.__dict__.update(news_dictionary)
        news.__dict__.update(author_dictionary)        
        news.body_content = body_content
        news.save()
        
        

    
    
