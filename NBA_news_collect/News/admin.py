from django.contrib import admin
from .models import News







class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'image_url', 'detail_url', 'post_date', 'author', 'detail', 'video_url')
admin.site.register(News, NewsAdmin)