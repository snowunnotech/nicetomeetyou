from django.contrib import admin

from .models import NBAframework

class NBANewsModelAdmin(admin.ModelAdmin):
    # display attributes in admin page
    list_display = ['id', 'title', 'publish_date', 'author', 'created', 'read']
    # filter list
    list_filter = ('read', 'created', 'publish_date')
    # search by *
    search_fields = ('title', 'content')
    ordering = ['publish_date', 'read']

admin.site.register(NBAframework, NBANewsModelAdmin)