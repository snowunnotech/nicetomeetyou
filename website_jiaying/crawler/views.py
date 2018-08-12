# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from pyquery import PyQuery as pq
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class news_content_crawler(APIView):

    def post(self, request, format=None):
        try:
            request_data = request.data
            NBA_url = request_data['url']
            html_doc = pq(NBA_url)
            author_css = ".shareBar__info--author"
            author = html_doc(author_css).text()
            content_css = "p"
            content = html_doc(content_css).text()
            jason_response = {
                "status": "ok",
                "description": "get news content successfully",
                "author": author,
                "content": content
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