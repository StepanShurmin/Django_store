from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Регистрирует модель для отображения в админке."""
    list_display = ('pk', 'name', 'description')
    list_filter = ('is_active',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрирует модель для отображения в админке."""
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
