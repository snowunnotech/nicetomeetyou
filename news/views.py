from django.shortcuts import render


def index(request, template='news/index.html'):

    return render(request, template)
