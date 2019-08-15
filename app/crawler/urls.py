from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('hello_world/', views.Hello.as_view()),
    path('nba_crawler/', views.Nba_Crawler.as_view()),
    # url(r'^show_result/(?P<newebpay_merchant_trade_no>[\w\x2D_]+)/$', views.Result.as_view()),
]