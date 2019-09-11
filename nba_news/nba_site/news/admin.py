from django.contrib import admin

# Register your models here.
from django.contrib import admin
from news.models import News

admin.site.register(News)