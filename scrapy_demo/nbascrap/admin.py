from django.contrib import admin
from .models import NbaNews

# Register your models here.
@admin.register(NbaNews)
class NbaNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_datetime')
