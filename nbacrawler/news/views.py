from django.shortcuts import render
# Create your views here.

def news_list(request):
    return render(request, 'news_list.html')