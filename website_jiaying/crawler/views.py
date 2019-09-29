# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from pyquery import PyQuery as pq
import logging
from .models import Post
from .serializers import PostSerializer

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class NewsContentCrawler(APIView):

    def get_news_content(self, url):
        try:
            html_doc = pq(url)
        except Exception as e:
            log.error(str(e))
            return False
        author_css = ".shareBar__info--author"
        content_css = "p"
        news_content = {
            "author" : html_doc(author_css).text(),
            "content" : html_doc(content_css).text()
        }
        return news_content

    def post(self, request, format=None):
        try:
            request_data = request.data
            NBA_url = request_data['url']
            news_content = self.get_news_content(NBA_url)
            if news_content is False:
                jason_response = {
                    "status": "error",
                    "description": "get news content error",
                    "author": "",
                    "content": ""
                }
                return Response(jason_response)
            jason_response = {
                "status": "ok",
                "description": "get news content successfully",
                "author": news_content["author"],
                "content": news_content["content"]
            }
        except Exception as e:
            log.error(str(e))
            jason_response = {
                "status": "error",
                "description": str(e),
                "author": "",
                "content": ""
            }
        return Response(jason_response)


class NewsListCrawler(APIView):

    def get(self, request, format=None):
        try:
            if self.get_news_list_and_content_save_to_db():
                last_four_news = Post.objects.all().order_by('-id')[:4]
                last_four_news_in_ascending_order = reversed(last_four_news)
                serializer = PostSerializer(last_four_news_in_ascending_order, many=True)
                jason_response = {
                    "status": "ok",
                    "description": "get news list successfully",
                    "news_list": serializer.data
                }
            else:
                jason_response = {
                    "status": "error",
                    "description": "get news list error",
                    "news_list": ""
                }
        except Exception as e:
            log.error(str(e))
            jason_response = {
                "status": "error",
                "description": str(e),
                "news_list": ""
            }
        return Response(jason_response)

    def get_news_list_and_content_save_to_db(self):
        for nba_news in self.get_nba_news_list():
            if not Post.objects.filter(title=nba_news['title']).exists():
                log.debug("New post : " + nba_news['title'])
                news_content = NewsContentCrawler()
                content = news_content.get_news_content(nba_news['link'])
                if content:
                    nba_news['author'] = content['author']
                    nba_news['content'] = content['content']
                    self.save_news_to_db(nba_news)
                    log.debug("saved" + nba_news['title'])
                    return True
                else:
                    return False
            else:
                return True

    def get_nba_news_list(self):
        NBA_url = "https://nba.udn.com/nba/index?gr=www"
        html_doc = pq(NBA_url)
        name_css = "#news_body a"
        NBA_html = html_doc(name_css)
        nba_news_list = []
        for item in NBA_html.items():
            news_item = item.text().split("\n")
            nba_news_list.append(
                {
                    "title": news_item[1],
                    "intro": news_item[2],
                    "link": "https://nba.udn.com" + item.attr['href'],
                    "photo": item("img").attr['src']
                }
            )
        return nba_news_list

    def save_news_to_db(self, news):
        news_obj = Post(
            title=news['title'],
            author = news['author'],
            intro=news['intro'],
            content = news['content'],
            link=news['link'],
            photo=news['photo']
        )
        news_obj.save()
        return news_obj

