from .serializers import ArticleSerializer
from main.models import imgnews
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ArticleListView(ListCreateAPIView):
    queryset = imgnews.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = imgnews.objects.all()
    serializer_class = ArticleSerializer
