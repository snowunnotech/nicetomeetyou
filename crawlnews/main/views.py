from django.shortcuts import render
from django.views import generic, View

# import tools
import requests
from bs4 import BeautifulSoup

# import class from models
from .models import News



# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class NewsListView(IndexView):
    template_name = 'newslist.html'
    
def NewsDetail(request, url_id):
    template_name = 'newsdetail.html'
    content = {
        "News" : News.objects.filter(url_id=url_id).first()
    } 
    return render(request, template_name, content)


def homepage(request):

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

        # get everything first
        news_dictionary = dict( zip(
            ["time", "title", "statement"], a_tag.stripped_strings
        ) )
        url_detail = a_tag.get("href")
        url_id = url_detail.split("/")[-1]
        image = a_tag.select_one("span.img-boxs img").get("src")
        # crawl another detail page
        Soup = BeautifulSoup( requests.get( host + url_detail ).text )
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
        content["news"].append(news_dictionary)        

    return render(request, "index.html", content)


