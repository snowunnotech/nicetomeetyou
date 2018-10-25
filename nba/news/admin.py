from django.contrib import admin
from .models import *
# Register your models here.

class newscatchAdmin (admin.ModelAdmin):
    list_display = ('title','time','cotent','img')

admin.site.register(newscatch,newscatchAdmin)