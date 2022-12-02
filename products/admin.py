from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'brand',
        'name',
        'sku',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
     )


class ReviewAdmin(admin.ModelAdmin):
    """
    class for admin to  manage review model
    """
    list_display = (
        'product',
        'author',
        'created_on',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
