from django.contrib import admin

# Register your models here.
from .models import NewsDetail, NewsIndex

admin.site.register(NewsDetail)
admin.site.register(NewsIndex)