# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from .models import NbaNews


# Create your views here.
def index(request):
    table = NbaNews.objects.all()
    return render_to_response('index.html', locals())


def update(request):
    print "called..."
    from . import scrape_udn
    news = scrape_udn.udn_nba_new()
    news_links = news.get_news_details_link()
    data = [scrape_udn.parsing_story(url) for url in news_links]

    conn = scrape_udn.sqlite3.connect("../db.sqlite3")
    try:
        query = """
            create table if not exists nba_news(
                info datetime,
                author varchar(100),
                title varchar(100),
                story varchar(100000)
            );
            """
        conn.execute(query)
        conn.commit()

        conn.executemany("insert into nba_news values(?, ?, ?, ?)", data)
        conn.commit()

    finally:
        conn.close()

    return render(request, 'index.html')
