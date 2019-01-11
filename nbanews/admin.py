from django.contrib import admin
from .models import Articles
# Register your models here.
@admin.register(Articles)
class ArticlesTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'text', 'time', 'img', 'detail')