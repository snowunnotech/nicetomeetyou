from django.contrib import admin
from mainsite.models import news_record
# Register your models here.

class news_recordAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(news_record,news_recordAdmin)