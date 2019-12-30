from django.conf.urls import url  #新增
from nba_news import views

# 嚴格匹配開頭結尾

urlpatterns = [
    url(r'^nba_news$', views.nba_news, name='nba_news'),  # 地方urls 進行匹配，正則須為index結尾
    # url(r'^getnews_detail/(?P<href>https?://\S+)', views.getnews_detail, name='getnews_detail'), # detail news
    url(r'^getnews_detail', views.getnews_detail, name='getnews_detail'),  # detail news

]
