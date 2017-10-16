from django.contrib import admin

# Register your models here.

from .models import Headline, Article

admin.site.register(Headline)
admin.site.register(Article)
