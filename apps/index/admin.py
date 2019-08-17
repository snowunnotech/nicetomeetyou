from django.contrib import admin
from .models import Feeds,News,NewsDetail

# Register your models here.

admin.site.register(Feeds)
admin.site.register(News)
admin.site.register(NewsDetail)
