from django.contrib import admin
from django.utils.safestring import mark_safe

from optics.models import (Brand, Category, Feedback, Product, Quote,
                           ResultOfService, Service)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'brand', 'price', 'category', 'image', 'photo_product', 'parameter', 'description', 'owner', 'is_published')
    list_display = ('id', 'brand', 'name', 'price', 'category', 'photo_product')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_display_links = ('name',)
    readonly_fields = ('photo_product',)
    ordering = ('brand', 'name',)
    save_on_top = True

    @admin.display(description="Просмотр")
    def photo_product(self, product: Product):
        if product.image:
            return mark_safe(f"<img src='{product.image.url}' width=50>")
        return "Без изображения"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(ResultOfService)
class ResultOfServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass
