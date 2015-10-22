from enum import IntEnum

from django.db import models
from django.utils import timezone


class Payment(models.Model):
    class STATE(IntEnum):
        CANCELLED = -1
        PENDING = 0
        DECLINED = 1
        APPROVED = 2
    order = models.ForeignKey('orders.Order')
    created = models.DateTimeField(default=timezone.now, editable=False)
    state = models.IntegerField(default=STATE.PENDING, choices=(
        (x.value, x.name.title())
        for x in STATE
    ))
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    reason = models.CharField(max_length=200, blank=True)
