from django.contrib import admin

from . import models


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'user',)
    list_filter = ('created',)

admin.site.register(models.Order, OrderAdmin)
