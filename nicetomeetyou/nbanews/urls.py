from django.conf.urls import include, url

from nbanews.views import GetNbaNewsList, GetNbaNewsDetail, news_list


urlpatterns = [
    url(r'^$', news_list),
    url(r'^newsapi/$', GetNbaNewsList.as_view()),
    url(r'^newsapi/(?P<newsid>[0-9]+)/$', GetNbaNewsDetail.as_view()),
]
