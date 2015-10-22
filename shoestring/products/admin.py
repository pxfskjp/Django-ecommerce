from django.contrib import admin

from . import models


class ImageInline(admin.TabularInline):
    model = models.Image
    extra = 0
    sortable_field_name = 'order'
    hidden_fields = ('order',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'enabled',)
    list_editable = ('enabled',)
    list_filter = ('enabled',)
    inlines = (
        ImageInline,
    )

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Brand)
