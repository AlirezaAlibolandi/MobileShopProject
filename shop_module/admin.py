from django.contrib import admin
from .models import Product, Category, Images, Company
# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['__all__']
#     list_filter = ['__all__']
#     search_fields = ['__all__']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)
admin.site.register(Company)
