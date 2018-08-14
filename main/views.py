from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import generics

from .models import News


class ListNews(generics.ListAPIView):
    '''
    Insert the newest news into database.
    List all the news on the home page.
    '''
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        queryset = News.objects.all()
        return Response({'newses': queryset}, template_name='main/home.html')


class RetrieveNews(generics.RetrieveAPIView):
    '''
    Show the detail of news with the JSON on the homepage
    '''
    renderer_classes = (JSONRenderer,)
    queryset = News.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        photos = self.object.photo_set.all()
        photo_list = []
        for photo in photos:
            photo_list.append({
                'alt': photo.alt,
                'src': photo.src,
                'description': photo.description
            })
        if request.is_ajax():
            return Response({
                'id': self.object.id,
                'content': self.object.content,
                'title': self.object.title,
                'url': self.object.url,
                'photo': photo_list
            })
        return redirect('news_list')
