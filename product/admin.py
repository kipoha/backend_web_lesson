from django.contrib import admin

# Register your models here.
from product.models import Product, Review, Category

# admin.site.register(Product)

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description', 'created')
    list_display_links = ('category_name',)
    list_filter = ('created',)
    search_fields = ('category_name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'created', 'category', 'author')
    list_display_links = ('product_name',)
    list_editable = ('category',)
    inlines = [ReviewInline]
    list_filter = ('category', 'created')