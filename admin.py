from django.contrib import admin

from django.contrib import admin
from .models import NewsCategory, News

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "content")
