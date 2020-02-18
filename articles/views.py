from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from scrap import prepare_soup, extract_content, extract_title, get_time, get_article_attribute, get_list_of_url
from .serializers import ArticleSerializer
from django.http import JsonResponse

def index(request):
    write_to_database()
    return render(request, 'articles/home.html')
    #return render(request, 'articles/home.html', context)
def get_list_of_article(request):
    '''
    return a list of object
    '''
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return JsonResponse(serializer.data, safe = False)

def article_detail(request, slug):
    article = Article.objects.get(slug = slug)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def write_to_database():
    '''
    parse headline from nba news. 
    In each news, extract detail and save to database
    '''
    url = 'https://nba.udn.com/nba'
    soup = prepare_soup(url)
    links = get_list_of_url(soup, url)
    for link in links:
        soup = prepare_soup(link)
        if not is_news_duplicated(link):
            date = get_time(soup)
            article_info = get_article_attribute(soup)
            title = extract_title(soup)      
            reporter = article_info.get('reporter', None)
            article_type = article_info.get('type', None)
            office = article_info.get('office', None)
            content = extract_content(soup)
            a = Article(
                title = title,
                author = reporter,
                date = date,
                category = article_type,
                office = office,
                content = content,
                url = link,
            )

            a.save()
    return None


def is_news_duplicated(url):
    a_count = Article.objects.filter(url = url).count()
    if a_count:
        return True
    else:
        return False

