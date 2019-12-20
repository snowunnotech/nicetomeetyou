from django.contrib import admin
from myapp.models import news
class newsAdmin(admin.ModelAdmin):
    list_display=('id','title','content','link_path','time')
    ordering=('id',)
# Register your models here.
admin.site.register(news,newsAdmin)