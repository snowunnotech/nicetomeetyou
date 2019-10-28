from django.urls import path
from .views import ArticleListView,  ArticleDetailView

urlpatterns = [
    path('article/', ArticleListView.as_view()),
    path('article/<pk>', ArticleDetailView.as_view()),


]
