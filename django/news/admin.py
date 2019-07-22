from django.contrib import admin
from .models import NBA
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'date_time',
                    'author',
                    'content',
                    'image_source',
                    'video_source',
                    'article_url')

admin.site.register(NBA, NewsAdmin)