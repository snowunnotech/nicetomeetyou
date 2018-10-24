from django.urls import path
from nbanews import views

urlpatterns = [
    path('', views.target_html),
    path('test/', views.get_news.as_view()),
    path('test/<int:pk>/', views.get_details.as_view()),
]