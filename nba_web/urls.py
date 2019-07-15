from django.urls import path
from . import views

urlpatterns = [
                path('', views.all_new_list, name='all_news'),
                path('<int:id>', views.news_list, name='news')
              ]
