from django.contrib import admin

from .models import Article


# create a table with specified columns in admin panel
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
            "text",
            "date",
            "author",
    ]

admin.site.register(Article, ArticleAdmin)
