from django.apps import apps

def GET_NBA_NEWS(items=3):
    NBANewsInFocus = apps.get_model('crawler','NBANewsInFocus')
    try:
        news = NBANewsInFocus.objects.order_by('-date_added')[0:items]
    except:
        news = NBANewsInFocus.objects.order_by('-date_added')[0:3]
    return news
def GET_NBA_NEWS_BYID(id):
    NBANewsInFocus = apps.get_model('crawler','NBANewsInFocus')
    try:
        news = NBANewsInFocus.objects.get(id=id)
        return news
    except:
        return None