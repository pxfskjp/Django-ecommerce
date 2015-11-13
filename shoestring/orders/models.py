from enum import IntEnum

from django.conf import settings
from django.db import models, transaction
from django.utils import timezone
from django.utils.functional import cached_property

from . import managers
from ..products.models import BaseProduct


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(default=timezone.now)

    shipping_address = models.TextField(blank=True)
    shipping_suburb = models.CharField(max_length=100, blank=True)
    shipping_postcode = models.CharField(max_length=6, blank=True)

    @classmethod
    def from_cart(self, user, cart):
        '''
        Build a new Order with items from a Cart
        '''
        with transaction.atomic():
            order = Order.objects.create(user=user)
            for item in cart.values():
                prod = item.product
                data = {
                    field.name: getattr(prod, field)
                    for field in BaseProduct._meta.get_fields()
                }
                OrderItem.objects.create(order=order, **data)
            return order


class OrderItem(BaseProduct):

    class STATE(IntEnum):
        CANCELLED = -1
        PENDING = 0
        SHIPPED = 1

    order = models.ForeignKey('Order', related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    status = models.IntegerField(choices=((x.value, x.name) for x in STATE),
                                 default=STATE.PENDING)

    objects = managers.OrderItemQuerySet.as_manager()

    @cached_property
    def total(self):
        return self.price * self.quantity
