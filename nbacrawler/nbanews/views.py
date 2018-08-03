from django.shortcuts import render


# Create your views here.

def list_view(request):
    return render(request, 'nbanews/list.html', {})


def detail_view(request, slug, id):
    print(id)
    return render(request, 'nbanews/detail.html', {'detail_id': id})
