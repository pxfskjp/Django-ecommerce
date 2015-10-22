
from django.utils.functional import cached_property
from nap import rpc
from nap.utils.ripper import Ripper

from .cart import Cart

CartItemRipper = Ripper('sku', 'qty', 'product')


class CartView(rpc.RPCView):

    @cached_property
    def cart(self):
        return Cart.from_session(self.request.session)

    def save(self):
        self.cart.save(self.request.session)

    @rpc.method
    def content(self):
        return {
            'total': self.cart.total(),
            'items': [
                CartItemRipper(item)
                for item in self.cart.values()
            ],
        }

    @rpc.method
    def add(self, sku, qty):
        '''
        Add an Item to the cart
        '''
        self.cart.add(sku, qty)
        self.save()
        return {}

    @rpc.method
    def quantity(self, sku, qty):
        '''
        Update quantity
        '''
        if qty == 0:
            self.cart.pop(sku)
            self.save()
        else:
            try:
                self.cart[sku].qty += qty
                self.save()
            except KeyError:
                raise ValueError('Item not in cart', sku)

        return {}

    def clear(self):
        '''
        Clear the cart.
        '''
        self.request.session.pop('cart')
        self.save()
        return {}
