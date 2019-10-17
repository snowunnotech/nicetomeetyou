from django.shortcuts import render

def list_view(request):
    return render(request, 'templates/NBAframework/list.html', {})

def detail_view(request, id):
    return render(request, 'NBAframework/detail.html', {'detail_id': id})
