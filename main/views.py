from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework import generics

from .models import News
# import crawl


class ListNews(generics.ListAPIView):
    '''
    Insert the newest news into database.
    List all the news on the home page.
    '''
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        # crawl.main()
        queryset = News.objects.all()
        return Response({'newses': queryset}, template_name='main/home.html')


class RetrieveNews(generics.RetrieveAPIView):
    '''
    Show the detail of news with the JSON on the homepage
    '''
    queryset = News.objects.all()
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({
            'id': self.object.id,
            'content': self.object.content,
            'title': self.object.title,
            'url': self.object.url,
        })
