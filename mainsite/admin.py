from django.contrib import admin
from .models import NewsInfo
# Register your models here.


class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(NewsInfo, NewsInfoAdmin)
