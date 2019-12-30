from django.contrib import admin
from nba_news.models import News
# 後臺管理相關
# Register your models here.

class News_admin(admin.ModelAdmin):
	''' member 返回輸出管理類 '''
	list_display = ['Title','Create_at']  # 顯示會員哪些資料
	list_filter = ('Title','Create_at')  # filter 按鈕
	search_fields = ('Title',)
	ordering = ('-Create_at',)


admin.site.register(News, News_admin)   # 註冊
