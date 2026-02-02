from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']
    # If you added a slug field to Product, uncomment the line below:
    # prepopulated_fields = {'slug': ('name',)}