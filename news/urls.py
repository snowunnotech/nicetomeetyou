from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from news.views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^$', TemplateView.as_view(template_name='news/index.html')),
    url(r'^news/(?P<pk>[0-9]+)/$', TemplateView.as_view(template_name='news/detail.html')),
]
