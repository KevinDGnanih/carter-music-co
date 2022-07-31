from django.contrib import admin
from .models import Product, Category, Brand



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'brand',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_brand_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
