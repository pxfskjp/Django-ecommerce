
from collections import OrderedDict

from django.apps import apps
from django.utils.functional import cached_property

Product = apps.get_model('products.Product')


class CartItem(object):

    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity

    @cached_property
    def product(self):
        return Product.objects.get(sku=self.sku)

    @property
    def total(self):
        return self.product.price * self.quantity


class Cart(OrderedDict):

    @classmethod
    def from_session(cls, session):
        # XXX This should pre-fetch products in a single query
        try:
            return cls(
                (item['sku'], CartItem(**item))
                for item in session.get('cart', [])
            )
        except TypeError:
            # Bad cart data
            session.pop('cart')
            return cls()

    def save(self, session):
        session['cart'] = [
            {'sku': item.sku, 'quantity': item.quantity}
            for item in self.values()
        ]

    def total(self):
        if not self:
            return 0
        return sum([item.total for item in self.values()])

    def add(self, sku, quantity=1):
        if sku not in self:
            self[sku] = CartItem(sku=sku, quantity=quantity)
        else:
            self[sku].quantity += quantity
