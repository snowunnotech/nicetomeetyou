from django.db import models


# class NewsManager(models.Manager):
#
#     def create(self, number, title, image, contents, published_date):
#         news = self.create(number=number, title=title, image=image, contents=contents, published_date=published_date)
#         return news


class News(models.Model):

    number = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    contents = models.TextField(null=True)
    published_date = models.DateTimeField(null=True)

    @classmethod
    def create(cls, number, title, image, contents, published_date):
        news = cls(number=number, title=title, image=image, contents=contents, published_date=published_date)
        return news




