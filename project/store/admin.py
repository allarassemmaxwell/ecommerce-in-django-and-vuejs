from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'date_added'
    list_display 		= ['title', 'date_added']
    list_display_links 	= ['title']
    list_filter 		= ['title']
    search_fields 		= ['title']
    readonly_fields		= ['date_added', 'date_updated']
    list_per_page 		= 25
    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    date_hierarchy      = 'date_added'
    list_display 		= ['title', 'date_added']
    list_display_links 	= ['title']
    list_filter 		= ['title']
    search_fields 		= ['title']
    readonly_fields		= ['date_added', 'date_updated']
    list_per_page 		= 25
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)



