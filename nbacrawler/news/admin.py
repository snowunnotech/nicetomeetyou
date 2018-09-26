from django.contrib import admin
from .models import News

@admin.register(News)
class BankAccountsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in News._meta.fields]