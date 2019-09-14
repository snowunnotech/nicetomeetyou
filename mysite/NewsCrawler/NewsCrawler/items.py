from scrapy_djangoitem import DjangoItem
from api.models import Article


class ArticleItem(DjangoItem):
    django_model = Article
