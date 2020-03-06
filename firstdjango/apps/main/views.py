from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from .models import Article


# Create your views here.

class FeedsView(View):
    def get(self, request):
        all_feeds = Article.objects.all()
        return render(request, 'index.html', {'all_feeds': all_feeds})
