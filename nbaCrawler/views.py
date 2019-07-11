from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import TemplateView
from selenium import webdriver
from bs4 import BeautifulSoup
from .models import Post
from .serializers import PostSerializer

# Create your views here.

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_date')
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)


class IndexView(TemplateView):
    template_name = "nbaCrawler/index.html"
