"""
./backend_app/admin.py
define admin page
"""
from django.contrib import admin
from .models import ArticleItem
# Register your models here.
@admin.register(ArticleItem)
class ArticleItemAdmin(admin.ModelAdmin):
    pass