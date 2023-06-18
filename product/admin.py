from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from product.models import Category, Product, Images, Comment

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 4


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['image_tag', 'title', 'status', 'create_at', 'slug']
#     list_filter = ['status']
#     readonly_fields = ('image_tag',)
#     list_display_links = ['image_tag', 'title']

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Product,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'title',
                    'category', 'price', 'status', 'slug']
    list_filter = ['status', 'category']
    inlines = [ProductImageInline]
    readonly_fields = ('image_tag',)
    list_display_links = ['image_tag', 'title']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'title', 'product']
    readonly_fields = ('image_tag',)
    list_display_links = ['image_tag', 'title', 'product']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'product', 'user', 'status']
    list_filter = ['status']
