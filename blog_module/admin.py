from django.contrib import admin

from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at', 'is_active')
    list_filter = ('category', 'tags', 'author', 'is_active')
    search_fields = ('title', 'description', 'short_description')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)