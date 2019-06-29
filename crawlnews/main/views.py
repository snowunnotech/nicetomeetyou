from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.

def homepage(request):

    response = requests.get("https://nba.udn.com/nba/index?gr=www")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    a_tags = soup.select("div#news_body dl > dt > a")

    content = {
        "news" : [],
    }
    
    for a_tag in a_tags :
        news_dictionary = dict( zip(
            ["time", "title", "statement"], a_tag.stripped_strings
        ) )
        content["news"].append(news_dictionary)
    

    return render(request, "index.html", content)
