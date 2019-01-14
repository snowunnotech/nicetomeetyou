"""
./backend_app/views.py
define views to render
"""
from rest_framework import generics
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import ArticleItem, TaskItem
from .serializers import ArticleItemSerializer, TaskItemSerializer, ArticleListSerializer

# class based views (CBV)
class ArticleListView(generics.ListAPIView):
    """
    API endpoint that allows articles to be viewed.
    Used for read-only endpoints to represent a collection of model instances.
    """
    # overrides the default get_queryset() method
    def get_queryset(self):
        articles = ArticleItem.objects.all().order_by('publish_dt')
        return articles
    serializer_class = ArticleListSerializer

class TaskListView(generics.ListAPIView):
    """
    API endpoint that allows tasks to be viewed.
    Used for read-only endpoints to represent a collection of model instances.
    """
    # overrides the default get_queryset() method
    def get_queryset(self):
        tasks = TaskItem.objects.all().order_by('created_dt')
        return tasks
    serializer_class = TaskItemSerializer

class TaskDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows a task to be viewed in detail.
    Used for read-only endpoints to represent a collection of model instances.
    """
    # overrides the default get_object() method
    def get_object(self):
        jobid = self.kwargs['jobid']
        task = TaskItem.objects.get(pk=jobid)
        return task
    # should be specified as the base for lookups in detail views (for the use of get_object())
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer

class ArticleDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows an article to be viewed in detail.
    Used for read-only endpoints to represent a collection of model instances.
    """
    # overrides the default get_object() method
    def get_object(self):
        pk = self.kwargs['pk']
        article = ArticleItem.objects.get(pk=pk)
        return article
    # should be specified as the base for lookups in detail views (for the use of get_object())
    queryset = ArticleItem.objects.all()
    serializer_class = ArticleItemSerializer

# function based views (FBV)
@require_http_methods(['GET']) # only get
def article_count(request):
    """ Return the total num of articles
    """
    if request.method == "GET":
        num = len(ArticleItem.objects.all())
        return JsonResponse({
            'num': num
        })
    return JsonResponse({
        'num': 'error'
    })
