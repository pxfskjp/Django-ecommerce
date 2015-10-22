from django.contrib import admin

from . import models


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'created', 'state', 'amount', 'reason')
    list_filter = ('order', 'state',)


admin.site.register(models.Payment, PaymentAdmin)
