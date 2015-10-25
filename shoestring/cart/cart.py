
from collections import OrderedDict

from django.apps import apps
from django.utils.functional import cached_property

Product = apps.get_model('products.Product')


class CartItem(object):

    def __init__(self, sku, qty):
        self.sku = sku
        self.qty = qty

    @cached_property
    def product(self):
        return Product.objects.get(sku=self.sku)

    @cached_property
    def total(self):
        return self.product.price * self.qty


class Cart(OrderedDict):

    @classmethod
    def from_session(cls, session):
        return cls(
            (item['sku'], CartItem(**item))
            for item in session.get('cart', [])
        )

    def save(self, session):
        session['cart'] = [
            {'sku': item.sku, 'qty': item.qty}
            for item in self.values()
        ]

    def total(self):
        if not self:
            return 0
        return sum([item.total for item in self.values()])

    def add(self, sku, qty=1):
        if sku not in self:
            self[sku] = CartItem(sku=sku, qty=qty)
        else:
            self[sku].qty += qty
