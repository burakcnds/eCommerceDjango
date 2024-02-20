from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','image','slug',]
    search_fields = ['name',]
    readonly_fields = ('slug',)


class DiscountProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','d_rate','d_price','image1','image2','image3','slug']
    search_fields = ['name']
    readonly_fields = ('slug',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','image1','image2','image3','slug']
 
admin.site.register(Category,CategoryAdmin)
admin.site.register(DiscountProduct,DiscountProductAdmin)
admin.site.register(Product,ProductAdmin)

