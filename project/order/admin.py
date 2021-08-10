from django.contrib import admin

# Register your models here.
from .models import *



# ORGANIZATION TYPE ADMIN
class OrderAdmin(admin.ModelAdmin):
    date_hierarchy      = 'created_at'
    list_display 		= ['email', 'first_name', 'last_name', 'created_at']
    list_display_links 	= ['email']
    list_filter 		= ['email', 'created_at']
    search_fields 		= ['email', 'created_at']
    readonly_fields		= ['created_at']
    list_per_page 		= 25
    class Meta:
        model = Order
admin.site.register(Order, OrderAdmin)




class OrderItemAdmin(admin.ModelAdmin):
    # date_hierarchy      = 'created_at'
    list_display 		= ['order', 'price', 'quantity']
    list_display_links 	= ['order']
    list_filter 		= ['order']
    search_fields 		= ['order']
    # readonly_fields		= ['created_at']
    list_per_page 		= 25
    class Meta:
        model = OrderItem
admin.site.register(OrderItem, OrderItemAdmin)
