from django.contrib import admin
from .models import Category, Product, ProductImage, ProductReview







# CATEGORY ADMIN 
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




# PRODUCT ADMIN 
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


# PRODUCT ADMIN 
class ProductImageAdmin(admin.ModelAdmin):
    date_hierarchy      = 'date_added'
    list_display        = ['id', 'date_added']
    list_display_links  = ['id']
    list_filter         = ['id']
    search_fields       = ['id']
    readonly_fields     = ['date_added', 'date_updated']
    list_per_page       = 25
    class Meta:
        model = ProductImage
admin.site.register(ProductImage, ProductImageAdmin)






admin.site.register(ProductReview)



