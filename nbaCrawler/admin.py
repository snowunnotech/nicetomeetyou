from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'pid', 'post_title', 'post_date', 'post_url')
    # list_filter = ['post_date']


admin.site.register(Post, PostAdmin)