from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
            "text",
            "date",
            "author",
    ]

admin.site.register(Article, ArticleAdmin)
