from django.contrib import admin
from .models import HotInfo


class HotInfoAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(HotInfo, HotInfoAdmin)
