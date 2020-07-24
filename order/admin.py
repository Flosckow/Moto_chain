from django.contrib import admin
from .models import Order, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ImportOrder(resources.ModelResource):
    class Meta:
        model = Order
        skip_unchanged = True
        report_skipped = True
        exclude = ('id')
        import_id_fields = ('title', 'image', 'price', 'description', 'category')


class OrderAdmin(ImportExportModelAdmin):
    resource_class = ImportOrder


admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
