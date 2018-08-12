from django.shortcuts import render

def news_index(request):
    return render(request, 'index.html')

