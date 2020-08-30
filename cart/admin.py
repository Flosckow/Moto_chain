from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import CartItem, Cart, OrderProduct



class OrderProductResource(resources.ModelResource):
    class Meta:
        model = OrderProduct
        fields = ('cart', 'status', 'is_active', 'date')


class OrderProductAdmin(ImportExportModelAdmin):
    resource_class = OrderProductResource


admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(OrderProduct, OrderProductAdmin)
