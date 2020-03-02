from django.shortcuts import render

# Create your views here.
# Create your views here.
from newsboard.models import NewsArticle
from newsboard.serializers import NewsBoardSerializer

from rest_framework import viewsets




# Create your views here.

def index(request):
	return render(request, 'newsboard/index.html')

class NewsBoardViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsBoardSerializer