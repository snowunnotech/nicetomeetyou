from django.contrib import admin
from .models import nbahotnews

class gameAdmin(admin.ModelAdmin):
    list_display = ('id', 'ntitle', 'nshortcnt', 'ncontent', 'nlink', 'nimglink', 'npubtime', 'nauth')

admin.site.register(nbahotnews ,gameAdmin)

# Register your models here.
