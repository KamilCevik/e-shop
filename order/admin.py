from django.contrib import admin
from order.models import ShopCart, OrderProduct, Order
# Register your models here.


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']
    list_display_links = ['user', 'product']


class OrderProductLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'city']
    list_filter = []
    readonly_fields = ('user', 'address', 'city', 'country',
                       'phone', 'first_name', 'ip', 'last_name')
    inlines = [OrderProductLine]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount',]
    list_filter = ['user']
