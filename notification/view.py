# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def news_feeds_index(request):
    return render(request, 'news_feeds.html', {})