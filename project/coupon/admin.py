from django.contrib import admin

# Register your models here.
from .models import *



# COUPON TYPE ADMIN
class CouponAdmin(admin.ModelAdmin):
    date_hierarchy      = 'created_at'
    list_display 		= ['code', 'value', 'active', 'created_at']
    list_display_links 	= ['code', 'value']
    list_filter 		= ['code', 'value']
    search_fields 		= ['code', 'value']
    readonly_fields		= ['created_at']
    list_per_page 		= 25
    class Meta:
        model = Coupon
admin.site.register(Coupon, CouponAdmin)

