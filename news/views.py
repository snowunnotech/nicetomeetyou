from django.shortcuts import render


def index(request, template='news/index.html'):

    return render(request, template)

def detail(request, pk, template='news/detail.html'):

    context = {
        'pk': pk
    }

    return render(request, template, context)
