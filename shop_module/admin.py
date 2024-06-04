from django.contrib import admin
from .models import Product, Category, Images, Company
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price','stock','company','is_active']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)
admin.site.register(Company)
